# this is an example for cortex release 0.14 and may not deploy correctly on other releases of cortex

labels = ["setosa", "versicolor", "virginica"]


class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        self.client = tensorflow_client

    def predict(self, payload):
        prediction = self.client.predict(payload)
        predicted_class_id = int(prediction["class_ids"][0])
        return labels[predicted_class_id]
