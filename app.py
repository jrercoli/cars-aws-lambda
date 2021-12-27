# import sys
import json
filename = "fake_cars.txt"

def handler(event, context):
    # fields in sample cars file
    car_fields = ['company', 'model']

    # output dict
    out_dict = {}

    # get the json event body, car requested
    print(event)
    # request_body = json.loads(event["body"]) if event.get("body") else json.loads(event)
    if event.get('car'):
        request_car = int(event['car'])
    else:
        request_car = 0
    print(request_car)

    with open(filename) as cars:
        # count var for car id creation
        car_id = 1

        for c in cars:
            reg = list(c.strip().split())

            # create dict with the fields
            car_dict = {}
            i = 0
            while i < len(car_fields):
                car_dict[car_fields[i]] = reg[i]
                i += 1
                # print(car_dict)

            # append the record of each car to output dict
            # check if request_car ( >0 ) else add all
            if request_car > 0:
                if car_id == request_car:
                    out_dict[str(car_id)] = car_dict
                    break
            else:
                out_dict[str(car_id)] = car_dict
            car_id += 1

    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(out_dict)
    }

    return response
    # return 'Hola desde AWS lambda con Python' + sys.version

