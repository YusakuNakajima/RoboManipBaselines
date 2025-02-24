import numpy as np
import pinocchio as pin
import gymnasium as gym
from robo_manip_baselines.common import MotionStatus
from .RolloutBase import RolloutBase


class RolloutMujocoAlohaCable(RolloutBase):
    def setup_env(self):
        self.env = gym.make(
            "robo_manip_baselines/MujocoAlohaCableEnv-v0", render_mode="human"
        )

    def set_arm_command(self):
        if self.data_manager.status in (MotionStatus.PRE_REACH, MotionStatus.REACH):
            target_pos = self.env.unwrapped.get_body_pose("B0")[0:3]
            target_pos[1] += 0.05  # [m]
            if self.data_manager.status == MotionStatus.PRE_REACH:
                target_pos[2] = 0.3  # [m]
                target_rpy = np.array([0.0, np.deg2rad(30), -np.pi / 2])
            elif self.data_manager.status == MotionStatus.REACH:
                target_pos[2] = 0.2  # [m]
                target_rpy = np.array([0.0, np.deg2rad(60), -np.pi / 2])
            self.motion_manager.target_se3 = pin.SE3(
                pin.rpy.rpyToMatrix(*target_rpy), target_pos
            )
            self.motion_manager.inverse_kinematics()
        else:
            super().set_arm_command()
