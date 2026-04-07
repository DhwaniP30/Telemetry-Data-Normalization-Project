# import the necessary modules and libraries
import json, unittest, datetime


def convertToMilliseconds(ts):
    dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

#use the open function to open read the three json files
# with open("./data-1.json","r") as f:
#     jsonData1 = json.load(f)
# with open("./data-2.json","r") as f:
#     jsonData2 = json.load(f)
# with open("./data-result.json","r") as f:
#     jsonExpectedResult = json.load(f)

with open("./data-1.json","r", encoding="utf-8") as f:
    jsonData1 = json.load(f)

with open("./data-2.json","r", encoding="utf-8") as f:
    jsonData2 = json.load(f)

with open("./data-result.json","r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)
# convert json data from format 1 to the expected format
def convertFromFormat1 (jsonObject):
    #solution


    locationParts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }
    #solution

    # IMPLEMENT: Conversion From Type 1

    

    

# convert json data from format 2 to the expected format


#solution 



   #solution
def convertFromFormat2(jsonObject):

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": convertToMilliseconds(jsonObject["timestamp"]),
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }
#solution



def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


# Test cases using unittest module
class TestSolution(unittest.TestCase):

    # Sanity test to ensure the expected result is as intended
    # converts json data to python objects usnig json.loads and json.dumps
    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    # run the tests
    unittest.main()