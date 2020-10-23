import cortex as c
import requests
import time

def main():
    print("testing")
    client = c.client("aws")
    for i in range(300):
        deployments = client.deploy(
            "/home/robert/projects/github/cortex/examples/batch/image-classifier/cortex.yaml",
            wait=True,
        )
        endpoint = deployments[0]["api"]["endpoint"]
        # time.sleep(10)

        response_raw = requests.delete(f"{endpoint}/1234")
        with open("logs.txt", "a+") as f:
            f.write(f"{i} {response_raw.text}")
        print(f"{i} {response_raw.text}")
        client.delete_api("image-classifier")
        # time.sleep(5)

if __name__ == "__main__":
    main()
