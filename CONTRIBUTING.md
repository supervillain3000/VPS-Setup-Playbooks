# Contributing

## Prerequisites
- Python 3.10+
- Docker (Molecule driver uses Docker containers)
- `git`

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install ansible ansible-lint molecule molecule-plugins[docker]
ansible-galaxy collection install -r requirements.yml
```

## Quality checks
```bash
ansible-lint
yamllint .
```

## Molecule usage
Run a single role scenario:
```bash
molecule test -s default -c roles/<role_name>/molecule/default/molecule.yml
```

Run all roles with Molecule:
```bash
./extentions/molecule/test-all-roles.sh
```

Run Molecule for one role using helper:
```bash
./extentions/molecule/test-all-roles.sh nginx
```

## Known limitations (macOS + Docker)
- Molecule runs Linux containers, not full VMs. Results can differ from real VPS hosts.
- Roles that depend on full `systemd` behavior may be flaky in containers.
- Firewall tasks (`ufw`, `firewalld`) can fail or be no-op in Docker; roles should support skipping firewall setup in containerized tests.
- Service/process checks in Molecule validate container behavior only; always run at least one end-to-end test on a real Linux VM before release.

## Adding a new role
1. Create role files:
```text
roles/<role_name>/
  defaults/main.yml
  tasks/main.yml
  handlers/main.yml
```
2. Follow current role pattern:
- Split OS-specific logic into `tasks/debian.yml` and `tasks/redhat.yml`.
- Keep defaults in `defaults/main.yml`.
- Add idempotent handlers in `handlers/main.yml`.
- Keep roles self-contained: install and configure prerequisites inside the role instead of relying on `base`.
- Only use role dependencies when explicit and documented.
3. Add Molecule scenario:
```text
roles/<role_name>/molecule/default/
  molecule.yml
  converge.yml
  verify.yml
```
4. In `converge.yml`, include the role directly and provide required vars.
5. Validate locally with:
```bash
molecule test -s default -c roles/<role_name>/molecule/default/molecule.yml
```

## Adding a new playbook
1. Add `playbooks/<name>.yml` with target role sequence.
2. Reuse role defaults where possible; expose only required vars.
3. Keep shared baseline roles (`base`, `sftp`) when relevant for VM provisioning.
4. Validate syntax:
```bash
ansible-playbook --syntax-check playbooks/<name>.yml
```

## Pull request checklist
- `ansible-lint` passes.
- Molecule passes for changed roles.
- New/updated role has `molecule/default` scenario.
- Docs updated if behavior or variables changed.
