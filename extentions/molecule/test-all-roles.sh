#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

if ! command -v molecule >/dev/null 2>&1; then
  echo "molecule is not installed. See CONTRIBUTING.md for setup."
  exit 1
fi

roles_with_molecule() {
  for role_dir in roles/*; do
    [[ -d "${role_dir}" ]] || continue
    [[ -f "${role_dir}/molecule/default/molecule.yml" ]] || continue
    basename "${role_dir}"
  done
}

ROLE_FILTER="${1:-}"

for role in $(roles_with_molecule); do
  if [[ -n "${ROLE_FILTER}" ]] && [[ "${role}" != "${ROLE_FILTER}" ]]; then
    continue
  fi
  echo "==> Running Molecule for role: ${role}"
  (
    cd "${ROOT_DIR}/roles/${role}"
    molecule test -s default
  )
done
