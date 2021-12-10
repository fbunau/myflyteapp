```
./docker_build_and_tag.sh -v workflow-v1

pyflyte --pkgs flyte.workflows package --image flyte:workflow-v1 -f\

flytectl register files --project flytesnacks --domain development --archive flyte-package.tgz --version V1 --k8sServiceAccount spark
```