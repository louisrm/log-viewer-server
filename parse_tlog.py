import os
import simplejson as json

def parse_tlog(filePath):
    """ execute mavlogdump.py and convert the output to a json object """ 

    # convert to json
    if os.name == 'nt':
        cmd = 'cmd /c "mavlogdump.py --show-seq --source-system 1 --format json "' + filePath + '" > output.json"'
    else:
        cmd = '"mavlogdump.py --show-seq --source-system 1 --format json "' + filePath + '" > output.json"'
        
    print('Executing: ' + cmd)
    os.system(cmd)

    # read json
    dataList = [json.loads(line) for line in open('output.json', 'r')]

    # parse into data dictionary
    data = {}
    data['MsgTime_s'] = []

    for dataLine in dataList:
        curType = dataLine['meta']['type']
        curTime = dataLine['meta']['timestamp']


        if curType in data:
            data[curType]['timestamp'].append(curTime)

            # append to total time and seq lists
            data['MsgTime_s'].append(curTime)

            dataDict = dataLine['data']
            for dataKey in dataDict:
                rawData = dataDict[dataKey]
                
                data[curType][dataKey].append(dataDict[dataKey])
        else:
            data[curType] = {}
            data[curType]['timestamp'] = [curTime]

            data['MsgTime_s'].append(curTime)

            dataDict = dataLine['data']
            for dataKey in dataDict:
                data[curType][dataKey] = [dataDict[dataKey]]

    json_object = json.dumps(data, ignore_nan = True) ## convert NaN's to null if present

    os.remove(os.path.join(os.getcwd(), 'output.json'))

    return json_object