from gymnasium.envs.registration import register

# Mujoco
## UR5e
register(
    id="multimodal_robot_model/MujocoUR5eCableEnv-v0",
    entry_point="multimodal_robot_model.envs.mujoco:MujocoUR5eCableEnv",
)
register(
    id="multimodal_robot_model/MujocoUR5eRingEnv-v0",
    entry_point="multimodal_robot_model.envs.mujoco:MujocoUR5eRingEnv",
)
register(
    id="multimodal_robot_model/MujocoUR5eParticleEnv-v0",
    entry_point="multimodal_robot_model.envs.mujoco:MujocoUR5eParticleEnv",
)
register(
    id="multimodal_robot_model/MujocoUR5eClothEnv-v0",
    entry_point="multimodal_robot_model.envs.mujoco:MujocoUR5eClothEnv",
)

## Aloha
register(
    id="multimodal_robot_model/MujocoAlohaCableEnv-v0",
    entry_point="multimodal_robot_model.envs.mujoco:MujocoAlohaCableEnv",
)

# Isaac
register(
    id="multimodal_robot_model/IsaacUR5eChainEnv-v0",
    entry_point="multimodal_robot_model.envs.isaac:IsaacUR5eChainEnv",
)
register(
    id="multimodal_robot_model/IsaacUR5eCabinetEnv-v0",
    entry_point="multimodal_robot_model.envs.isaac:IsaacUR5eCabinetEnv",
)

# Real
register(
    id="multimodal_robot_model/RealUR5eGearEnv-v0",
    entry_point="multimodal_robot_model.envs.real:RealUR5eGearEnv",
)
