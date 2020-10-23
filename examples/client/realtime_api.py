import cortex as c
import requests
import time

def main():
    print("testing")
    client = c.client("aws")
    for i in range(500):
        deployments = client.deploy("/home/robert/projects/github/cortex/examples/pytorch/iris-classifier/cortex.yaml", wait=True)
        url = deployments[0]["api"]["endpoint"]
        response = requests.get(url).text
        with open("sleep_in_tester_only", "a+") as f:
            f.write(str(i) + response + "\n")
        print(i, response)
        client.delete_api("iris-classifier")
        time.sleep(1)

if __name__ == "__main__":
    main()
