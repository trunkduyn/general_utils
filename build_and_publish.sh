#!/usr/bin/env bash
rm -rf build dist trunky_general_utils.egg-info
python setup.py sdist bdist_wheel
echo "destination dir: $TRUNKIE_WHEEL_DIR"
cp "dist/trunky_"*".whl" $TRUNKIE_WHEEL_DIR
rm -rf build dist trunky_general_utilsd.egg-info
