cd ~/RoboManipBaselines

sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf

pip install -e .
pip install -e .[act]
pip install -e .[sarnn]
pip install -e .[diffusion-policy]


cd ~/RoboManipBaselines/third_party/eipl
pip install -e .
cd ~/RoboManipBaselines/third_party/act/detr
pip install -e .
cd ~/RoboManipBaselines/third_party/r3m
pip install -e .
cd ~/RoboManipBaselines/third_party/diffusion_policy
pip install -e .
cd ~/RoboManipBaselines/third_party/gello_software
pip install -e .

cd ~/RoboManipBaselines