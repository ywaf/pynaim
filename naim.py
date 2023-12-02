import requests

class utils:
    def naim_get(self, host, port, path):
        try:
            resp = requests.get(f"http://{str(host)}:{str(port)}/{str(path)}")
            if resp.status_code == 200:
                return resp
        except Exception as e:
            print("exception!" + str(e))
            return False

    def naim_put(self, host, port, path, key_value: list):
        final_list = ""
        output_list = []
        for i in range(0, len(key_value), 2):
            if i + 1 < len(key_value):
                query_param = f"?{key_value[i]}={key_value[i + 1]}"
                output_list.append(query_param)
        for x in output_list:
            final_list = final_list + str(x)
        print(final_list)
        try:
            resp = requests.put(f"http://{str(host)}:{str(port)}/{str(path)}{final_list}")
            if resp.status_code == 200:
                return resp
        except Exception as e:
            print("exception!" + str(e))
            return False

class naim:
    def __init__(self, ip_address, port = "15081"):
        self.ip_address = ip_address
        self.port = port

    def status(self):
        return utils.naim_get(self, host=self.ip_address, port=self.port, path="system")

    def power_status(self):
        response = utils.naim_get(self, host=self.ip_address, port=self.port, path="power")
        try:
            response_json = response.json()
        except Exception as e:
            print("INVALID JSON RETURNED BY SERVER :(")
            print(e)
            return False

        if "state" in response_json:
            # print("ok")
            if response_json["state"] == "lona" or response_json["state"] == "switching_lona":
                return "off"
            elif response_json["state"] == "on" or response_json["state"] == "switching_on":
                return "on"
            else:
                return False



    def set_power(self, state: bool):
        utils.naim_put(self, host=self.ip_address, port=self.port, path="power", key_value=["system", "lona" if not state else "on"])
        mapping = {"on": True, "off": False}
        return state == mapping[self.power_status()]


    def get_source(self):
        response = utils.naim_get(self, host=self.ip_address, port=self.port, path="nowplaying")
        print(response.text)
        try:
            response_json = response.json()
        except Exception as e:
            print("INVALID JSON RETURNED BY SERVER :(")
            print(e)
            return False
        return response_json["source"]

    def set_source(self, target: str):
        print("a")


    def play(self):
        utils.naim_get(self, host=self.ip_address, port=self.port, path="")




