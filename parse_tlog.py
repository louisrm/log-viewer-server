import os
import simplejson as json

def parse_tlog(filePath):

    # convert to json
    cmd = 'cmd /c "mavlogdump.py --show-seq --source-system 1 --format json "' + filePath + '" > output.json"'
    print('Executing: ' + cmd)
    os.system(cmd)


    # read json
    dataList = [json.loads(line) for line in open('output.json', 'r')]

    # parse into data dictionary
    data = {}
    data['MsgTime_s'] = []
    #totalSeqList = []

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

    json_object = json.dumps(data, ignore_nan = True) 
    os.remove(os.path.join(os.getcwd(), 'output.json'))


    return json_object