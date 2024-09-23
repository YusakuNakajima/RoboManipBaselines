import numpy as np
import gymnasium as gym
import pinocchio as pin
import multimodal_robot_model
from multimodal_robot_model.teleop import TeleopBase
from multimodal_robot_model.common import RecordStatus

class TeleopMujocoUR5eParticle(TeleopBase):
    def __init__(self):
        super().__init__()

        # Command configuration
        self.command_rpy_scale = 1e-2

    def setupEnv(self):
        self.env = gym.make(
            "multimodal_robot_model/MujocoUR5eParticleEnv-v0",
            render_mode="human"
        )
        self.demo_name = "MujocoUR5eParticle"

    def setArmCommand(self):
        if self.record_manager.status in (RecordStatus.PRE_REACH, RecordStatus.REACH):
            target_pos = self.env.unwrapped.get_geom_pose("scoop_handle")[0:3]
            if self.record_manager.status == RecordStatus.PRE_REACH:
                target_pos += np.array([0.0, 0.0, 0.2]) # [m]
            elif self.record_manager.status == RecordStatus.REACH:
                target_pos += np.array([0.0, 0.0, 0.15]) # [m]
            self.motion_manager.target_se3 = pin.SE3(pin.rpy.rpyToMatrix(np.pi, 0.0, np.pi/2), target_pos)
        else:
            super().setArmCommand()

if __name__ == "__main__":
    teleop = TeleopMujocoUR5eParticle()
    teleop.run()
