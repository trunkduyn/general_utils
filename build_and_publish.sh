#!/usr/bin/env bash
rm -rf build dist trunky_template_repository.egg-info
python setup.py sdist bdist_wheel
echo "dir found: "
echo $TRUNKIE_WHEEL_DIR
cp "dist/trunky_"*".whl" $TRUNKIE_WHEEL_DIR
rm -rf build dist trunky_template_repositoryd.egg-info
