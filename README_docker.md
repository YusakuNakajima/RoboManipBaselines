### RoboManipBaselines Docker Setup README

#### Overview
This Docker setup is designed for the **RoboManipBaselines** project, focusing on utilizing dependencies required by the **DiffusionPolicy**. The Docker image `FROM nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04` is selected to provide GPU support and ensure compatibility with various dependencies.

During the setup, several issues were encountered, including difficulties with managing dependencies using `pip install -e .[diffusion-policy]`. To address this, a `requirements.txt` file has been created to streamline the dependency management process.

Additionally, an issue with installing `egl_probe` was resolved by enhancing CMake, as outlined in this GitHub issue:
- [egl_probe Installation Issue](https://github.com/StanfordVL/egl_probe/issues/2)

#### Steps for Setting Up Docker

1. **Base Docker Image**:
   - `FROM nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04` – A CUDA-enabled Ubuntu image optimized for GPU computing with CUDNN support.

2. **Dependencies Installation**:
   - Install essential libraries for running DiffusionPolicy:
     ```bash
     sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
     ```

3. **Requirements Management**:
   - Use `requirements.txt` for managing dependencies. Pyproject.toml was not recognized smoothly with the `pip install -e .[diffusion-policy]` command. 
     ```bash
     pip install -r requirements.txt
     ```

4. **Resolving Installation Issues**:
   - Addressing the `egl_probe` installation problem by enhancing CMake:
     ```bash
     pip install -e .[diffusion-policy]
     ```
     For more details, visit:
     [egl_probe Installation Issue](https://github.com/StanfordVL/egl_probe/issues/2)

#### Running the Docker Container

To run the Docker container with all necessary configurations:

```bash
docker run --gpus=all --name nakajima-robo-manip-baseline-1 --shm-size=64G -v ./:/home/user/RoboManipBaselines -it robo_manip_baseline:latest /bin/bash
```

This command will start a Docker container with access to GPUs, shared memory, and bind the current directory to the container's `/home/user/RoboManipBaselines`.

---

### Notes:
- Ensure that your system has sufficient GPU resources if using GPU acceleration.
- Adjust the shared memory size (`--shm-size`) as needed based on the scale of your tasks.
- Modify the volume mapping (`-v`) to point to the appropriate directory structure for your RoboManipBaselines project.


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

