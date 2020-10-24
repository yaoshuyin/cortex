import cortex as c
import requests
import time
import os


def main():
    print("testing")
    client = c.client("aws")

    try:
        os.remove("logs.txt")
    except:
        pass

    for i in range(500):
        deployments = client.deploy(
            "/home/ubuntu/src/github.com/cortexlabs/cortex/examples/pytorch/iris-classifier/cortex.yaml",
            wait=True,
        )
        url = deployments[0]["api"]["endpoint"]

        while True:
            raw_response = requests.get(url)
            with open("logs.txt", "a+") as f:
                f.write(f"{i} {raw_response.text}\n")
            print(f"{i} {raw_response.text}")
            if raw_response.status_code == 200:
                break
            print("retrying...")
            time.sleep(1)

        client.delete_api("iris-classifier")


if __name__ == "__main__":
    main()
