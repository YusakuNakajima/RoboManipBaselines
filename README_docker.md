### README for RoboManipBaselines Docker Setup

#### Overview
This Docker setup is tailored for the RoboManipBaselines project, specifically using DiffusionPolicy dependencies. To ensure smooth execution of required packages such as `sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf`, the Docker image `FROM nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04` is employed.

Additionally, issues were encountered when trying to use `pip install -e .[diffusion-policy]` due to pyproject.toml not being recognized properly. Therefore, a `requirements.txt` file was created to manage dependencies effectively.

Furthermore, an issue was resolved related to installing `egl_probe`. The solution involved enhancing CMake as described in this GitHub issue:
- [egl_probe Installation Issue](https://github.com/StanfordVL/egl_probe/issues/2)

#### Steps for Setting Up Docker

1. **Base Docker Image**:
   - `FROM nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04`

2. **Dependencies Installation**:
   - Required packages for DiffusionPolicy:
     ```bash
     sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
     ```

3. **Requirements Management**:
   - `requirements.txt` is used for dependency management as pyproject.toml was not recognized smoothly with the `pip install -e .[diffusion-policy]` command.

4. **Additional Tools**:
   - Resolving issues with `egl_probe` by enhancing CMake as described [here](https://github.com/StanfordVL/egl_probe/issues/2). 

This setup ensures that all necessary dependencies for RoboManipBaselines, including those required by DiffusionPolicy, are installed and managed effectively within the Docker environment.


## Train and run
### Diffusion policy
You can see here robo_manip_baselines/diffusion_policy/README.md
#### Dataset preparation
python ../utils/convert_npz_to_zarr.py \
--in_dir ../teleop/teleop_data/TeleopMujocoUR5eParticle_Dataset30_20241031 --out_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031.zarr \
--nproc `nproc` --skip 3

#### Model training
python ./bin/TrainDiffusionPolicy.py \
task.dataset.zarr_path=./data/TeleopMujocoUR5eParticle_Dataset30_20241031.zarr task.name=TeleopMujocoUR5eParticle_Dataset30_20241031

### SARNN
python ../utils/make_dataset.py \
--in_dir ../teleop/teleop_data/TeleopMujocoUR5eParticle_Dataset30_20241031 --out_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 \
--train_ratio 0.8 --nproc `nproc` --skip 6 --cropped_img_size 280 --resized_img_size 64


python ./bin/TrainSarnn.py \
--data_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 --log_dir ./log/TeleopMujocoUR5eParticle_Dataset30_20241031 \
--no_side_image --no_wrench --with_mask

