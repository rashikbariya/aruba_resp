import timeit
import json

import time

from central_ap import CentralApi


def main():
    file_out = f'{time.strftime("%Y%m%d-%H%M%S")}.txt'
    print('filename:', file_out)
    t = CentralApi()

    print('getting aps info....')
    aps = t.get_ap()["aps"]

    aps_dict = {}
    for ap in aps:
        aps_dict[ap["serial"]] = ap["name"]
    print('No. of APs:', len(aps_dict))

    print('Getting a clients connected to an AP...')
    for s_n, ap_name in aps_dict.items():
        params = {
            "serial": s_n,
        }
        client_info = t.get_clients(params)

        if client_info["count"] > 0:
            for client in client_info["clients"]:
                client["associated_device_name"] = ap_name

            print('writing to file')
            with open(f"{file_out}", "a") as file:
                file.writelines(json.dumps(client_info) + "\n")


if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print("Time taken to run the script is:", stop - start)
