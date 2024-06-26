import torch
import math
import roma

class RandomRotation(torch.nn.Module):
    def random_rotation(self, num_samples: int):
        angles = torch.random.uniform(
            -math.pi,
            math.pi,
            shape=(num_samples,)
        )
        rotmat= roma.euler_to_rotmat(
            "xyz",
            angles=angles,
        )
        return rotmat

    def forward(
            self,
            X: torch.nn.Tensor,
            num_samples: int,
    ):
        # (NUM_SAMPLES, 3, 3)
        R = self.random_rotation(num_samples)

        # (NUM_SAMPLES, N, 3)
        X = torch.einsum(
            "na, sab -> snb",
            X,
            R,
        )

        return X
        