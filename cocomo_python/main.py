
from flask import request, Flask, jsonify

app = Flask(__name__)

def fround (x):
    x = round(x)
    return(x)


def intermediate_calculate(table, n, mode, size, cost_driver, rq_reli, size_db, comp_p, run_cons, mem_cons, volatility, req_time, analys_cap, app_exp, se_cap, vm_exp, pl_exp, se_method, use_sw, dev_sch):
    if size >= 2 and size <= 50:
        model = 0
    elif size > 50 and size <= 300:
        model = 1
    elif size > 300:
        model = 2
        
    if size_db < 1:
        print("Rating for size_db 1-4 only")
        return(['NA', -1, -1, -1])
    elif run_cons < 2:
        print("Rating for run_cons 2-4 only")
        return(['NA', -1, -1, -1])
    elif mem_cons < 2:
        print("Rating for mem_cons 2-4 only")
        return(['NA', -1, -1, -1])
    elif volatility < 1:
        print("Rating for volatility 1-4 only")
        return(['NA',  -1, -1, -1])
    elif req_time < 1:
        print("Rating for req_time 1-4 only")
        return(['NA',  -1, -1, -1])
    elif vm_exp > 3:
        print("Rating for vm_exp 1-4 only")
        return(['NA',  -1, -1, -1])
    elif pl_exp > 3:
        print("Rating for vm_exp 1-4 only")
        return(['NA',  -1, -1, -1])
    
    eaf = cost_driver[0][rq_reli]*cost_driver[1][size_db]*cost_driver[2][comp_p]*cost_driver[3][run_cons]*cost_driver[4][mem_cons]*cost_driver[5][volatility]*cost_driver[6][req_time]*cost_driver[7][analys_cap]*cost_driver[8][app_exp]*cost_driver[9][se_cap]*cost_driver[10][vm_exp]*cost_driver[11][pl_exp]*cost_driver[12][se_method]*cost_driver[13][use_sw]*cost_driver[14][dev_sch]

    printout = (f'''
    The mode is {mode[model]}''')

    effort = table[model][0]* (size**table[model][1])*eaf 

    time = table[model][2]* (effort**table[model][3]) 

    staff = effort/time

    printout += f'''
    Effort = {round(effort, 3)} Person-Month
    Development Time = {round(time, 5)} Months
    Average Staff Required {fround(staff)} Persons
    '''
    print(printout)

    result = [mode[model], round(effort, 3), round(time, 5), fround(staff)]

    return(result)


@app.route('/', methods=['GET', 'POST'])
def get():
    
    data= request.json

    size = data['size']
    rq_reli = data['requiredSoftwareReliability']
    size_db = data['sizeofApplicationDatabase']
    comp_p = data['complexityofTheProduct']
    run_cons = data['runtimePerformanceConstraints']
    mem_cons = data['memoryConstraints']
    volatility = data['volatilityOfTheVirtualMachineEnvironment']
    req_time = data['requiredTurnaboutTime']
    analys_cap = data['analystCapability']
    app_exp = data['applicationsExperience']
    se_cap = data['softwareEngineerCapability']
    vm_exp = data['virtualMachineExperience']
    pl_exp = data['programmingLanguageExperience']
    se_method = data['applicationOfSoftwareEngineeringMethods']
    use_sw = data['useOfSoftwareTools']
    dev_sch = data['requiredDevelopmentSchedule']
    
    table = [
        [2.4,1.05,2.5,0.38],
        [3.0,1.12,2.5,0.35],
        [3.6,1.20,2.5,0.32]
    ]

    cost_driver = [
        [0.75, 0.88, 1.00, 1.15, 1.40],
        [-1, 0.94, 1.00, 1.08, 1.16],
        [0.70, 0.85, 1.00, 1.15, 1.30],
        [-1, -1, 1.00, 1.11, 1.30],
        [-1, -1, 1.00, 1.06, 1.21],
        [-1, 0.87, 1.00, 1.15, 1.30],
        [-1, 0.94, 1.00, 1.07, 1.15],
        [1.46, 1.19, 1.00, 0.86, 0.71],
        [1.29, 1.13, 1.00, 0.91, 0.82],
        [1.42, 1.17, 1.00, 0.86, 0.70],
        [1.21, 1.10, 1.00, 0.90, -1],
        [1.14, 1.07, 1.00, 0.95, -1],
        [1.24, 1.10, 1.00, 0.91, 0.82],
        [1.24, 1.10, 1.00, 0.91, 0.83],
        [1.23, 1.08, 1.00, 1.04, 1.10]
    ]

    mode = ["Organic","Semi-Detached","Embedded"]

    da_cost = intermediate_calculate(table,3,mode,size,cost_driver, rq_reli, size_db, comp_p, run_cons, mem_cons, volatility, req_time, analys_cap, app_exp, se_cap, vm_exp, pl_exp, se_method, use_sw, dev_sch)

    return(
        jsonify({"mode":da_cost[0], "effort":da_cost[1], "time":da_cost[2], "avg_staff":da_cost[3]})
    )
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

                                                                                                              
