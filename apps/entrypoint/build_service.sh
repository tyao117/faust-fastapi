set -o errexit

SCRIPTDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build -t tyao117/fast-api-sample-v1 --build-arg service_version=v1 "${SCRIPTDIR}"
