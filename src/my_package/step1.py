import torch


def runstep(arg: str = None):
    print(f"Step 1 {arg}!")
    t = torch.Tensor([1, 2, 3])
    print(t)
    print("update job task code")


if __name__ == "__main__":
    runstep()
