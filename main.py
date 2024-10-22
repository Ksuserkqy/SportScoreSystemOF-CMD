from json import load;
from os.path import abspath, dirname;

standardFile = "Standard.json"
programPath = abspath(dirname(__file__))

# 定义颜色
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


outputSign = "-" * 20
print(f"{outputSign}{Colors.BOLD}SSS-CMD v1.1.0 24w26a{Colors.ENDC}{outputSign}")
print(f"{outputSign}Made by {Colors.YELLOW}Ksuserkqy{Colors.ENDC} 2024.6.24{outputSign}\n")

try:
    with open(r"{}\{}".format(programPath, standardFile),'r',encoding='UTF-8') as f:
        sstandard = load(f);
    print("[SSS-CMD] 检测到外置评分标准 Standard.json，已使用该标准");
except:
    sstandard = {'男': {'立定跳远': [{'1': {'100': 260, '95': 255, '90': 250, '85': 243, '80': 235, '78': 231, '76': 227, '74': 223, '72': 219, '70': 215, '68': 211, '66': 207, '64': 203, '62': 199, '60': 195, '50': 190, '40': 185, '30': 180, '20': 175, '10': 170}, '2': {'100': 265, '95': 260, '90': 255, '85': 248, '80': 240, '78': 236, '76': 232, '74': 228, '72': 224, '70': 220, '68': 216, '66': 212, '64': 208, '62': 204, '60': 200, '50': 195, '40': 190, '30': 185, '20': 180, '10': 175}, '3': {'100': 270, '95': 265, '90': 260, '85': 253, '80': 245, '78': 241, '76': 237, '74': 233, '72': 229, '70': 225, '68': 221, '66': 217, '64': 213, '62': 209, '60': 205, '50': 200, '40': 195, '30': 190, '20': 185, '10': 180}}, 'num'], '引体向上': [{'1': {'100': 16, '95': 15, '90': 14, '85': 13, '80': 12, '76': 11, '72': 10, '68': 9, '64': 8, '60': 7, '50': 6, '40': 5, '30': 4, '20': 3, '10': 2}, '2': {'100': 17, '95': 16, '90': 15, '85': 14, '80': 13, '76': 12, '72': 11, '68': 10, '64': 9, '60': 8, '50': 7, '40': 6, '30': 5, '20': 4, '10': 3}, '3': {'100': 18, '95': 17, '90': 16, '85': 15, '80': 14, '76': 13, '72': 12, '68': 11, '64': 10, '60': 9, '50': 8, '40': 7, '30': 6, '20': 5, '10': 4}}, 'num'], '坐位体前屈': [{'1': {'100': 23.6, '95': 21.5, '90': 19.4, '85': 17.2, '80': 15.0, '78': 13.6, '76': 12.2, '74': 10.8, '72': 9.4, '70': 8.0, '68': 6.6, '66': 5.2, '64': 3.8, '62': 2.4, '60': 1.0, '50': 0.0, '40': -1.0, '30': -2.0, '20': -3.0, '10': -4.0}, '2': {'100': 24.3, '95': 22.4, '90': 20.5, '85': 18.3, '80': 16.1, '78': 14.7, '76': 13.3, '74': 11.9, '72': 10.5, '70': 9.1, '68': 7.7, '66': 6.3, '64': 4.9, '62': 3.5, '60': 2.1, '50': 1.1, '40': 0.1, '30': -0.9, '20': -1.9, '10': -2.9}, '3': {'100': 24.6, '95': 22.8, '90': 21.0, '85': 19.1, '80': 17.2, '78': 15.8, '76': 14.4, '74': 13.0, '72': 11.6, '70': 10.2, '68': 8.8, '66': 7.4, '64': 6.0, '62': 4.6, '60': 3.2, '50': 2.2, '40': 1.2, '30': 0.2, '20': -0.8, '10': -1.8}}, 'num'], '50米': [{'1': {'100': 7.1, '95': 7.2, '90': 7.3, '85': 7.4, '80': 7.5, '78': 7.7, '76': 7.9, '74': 8.1, '72': 8.3, '70': 8.5, '68': 8.7, '66': 8.9, '64': 9.1, '62': 9.3, '60': 9.5, '50': 9.7, '40': 9.9, '30': 10.1, '20': 10.3, '10': 10.5}, '2': {'100': 7.0, '95': 7.1, '90': 7.2, '85': 7.3, '80': 7.4, '78': 7.6, '76': 7.8, '74': 8.0, '72': 8.2, '70': 8.4, '68': 8.6, '66': 8.8, '64': 9.0, '62': 9.2, '60': 9.4, '50': 9.6, '40': 9.8, '30': 10.0, '20': 10.2, '10': 10.4}, '3': {'100': 6.8, '95': 6.9, '90': 7.0, '85': 7.1, '80': 7.2, '78': 7.4, '76': 7.6, '74': 7.8, '72': 8.0, '70': 8.2, '68': 8.4, '66': 8.6, '64': 8.8, '62': 9.0, '60': 9.2, '50': 9.4, '40': 9.6, '30': 9.8, '20': 10.0, '10': 10.2}}, 'time-short'], '1000米': [{'1': {'100': '3\'30"', '95': '3\'35"', '90': '3\'40"', '85': '3\'47"', '80': '3\'55"', '78': '4\'00"', '76': '4\'05"', '74': '4\'10"', '72': '4\'15"', '70': '4\'20"', '68': '4\'25"', '66': '4\'30"', '64': '4\'35"', '62': '4\'40"', '60': '4\'45"', '50': '5\'05"', '40': '5\'25"', '30': '5\'45"', '20': '6\'05"', '10': '6\'25"'}, '2': {'100': '3\'25"', '95': '3\'30"', '90': '3\'35"', '85': '3\'42"', '80': '3\'50"', '78': '3\'55"', '76': '4\'00"', '74': '4\'05"', '72': '4\'10"', '70': '4\'15"', '68': '4\'20"', '66': '4\'25"', '64': '4\'30"', '62': '4\'35"', '60': '4\'40"', '50': '5\'00"', '40': '5\'20"', '30': '5\'40"', '20': '6\'00"', '10': '6\'20"'}, '3': {'100': '3\'20"', '95': '3\'25"', '90': '3\'30"', '85': '3\'37"', '80': '3\'45"', '78': '3\'50"', '76': '3\'55"', '74': '4\'00"', '72': '4\'05"', '70': '4\'10"', '68': '4\'15"', '66': '4\'20"', '64': '4\'25"', '62': '4\'30"', '60': '4\'35"', '50': '4\'55"', '40': '5\'15"', '30': '5\'35"', '20': '5\'55"', '10': '6\'15"'}}, 'time-long'], '肺活量': [{'1': {'100': 4540, '95': 4420, '90': 4300, '85': 4050, '80': 3800, '78': 3680, '76': 3560, '74': 3440, '72': 3320, '70': 3200, '68': 3080, '66': 2960, '64': 2840, '62': 2720, '60': 2600, '50': 2470, '40': 2340, '30': 2210, '20': 2080, '10': 1950}, '2': {'100': 4740, '95': 4620, '90': 4500, '85': 4250, '80': 4000, '78': 3880, '76': 3760, '74': 3640, '72': 3520, '70': 3400, '68': 3280, '66': 3160, '64': 3040, '62': 2920, '60': 2800, '50': 2660, '40': 2520, '30': 2380, '20': 2240, '10': 2100}, '3': {'100': 4940, '95': 4820, '90': 4700, '85': 4450, '80': 4200, '78': 4080, '76': 3960, '74': 3840, '72': 3720, '70': 3600, '68': 3480, '66': 3360, '64': 3240, '62': 3120, '60': 3000, '50': 2850, '40': 2700, '30': 2550, '20': 2400, '10': 2250}}, 'num']}, '女': {'立定跳远': [{'1': {'100': 204, '95': 198, '90': 192, '85': 185, '80': 178, '78': 175, '76': 172, '74': 169, '72': 166, '70': 163, '68': 160, '66': 157, '64': 154, '62': 151, '60': 148, '50': 143, '40': 138, '30': 133, '20': 128, '10': 123}, '2': {'100': 205, '95': 199, '90': 193, '85': 186, '80': 179, '78': 176, '76': 173, '74': 170, '72': 167, '70': 164, '68': 161, '66': 158, '64': 155, '62': 152, '60': 150, '50': 144, '40': 139, '30': 134, '20': 129, '10': 124}, '3': {'100': 206, '95': 200, '90': 194, '85': 187, '80': 180, '78': 177, '76': 174, '74': 171, '72': 168, '70': 165, '68': 162, '66': 159, '64': 156, '62': 153, '60': 150, '50': 145, '40': 140, '30': 135, '20': 130, '10': 125}}, 'num'], '仰卧起坐': [{'1': {'100': 53, '95': 51, '90': 49, '85': 46, '80': 43, '78': 41, '76': 39, '74': 37, '72': 35, '70': 33, '68': 31, '66': 29, '64': 27, '62': 25, '60': 23, '50': 21, '40': 19, '30': 17, '20': 15, '10': 13}, '2': {'100': 54, '95': 52, '90': 50, '85': 47, '80': 44, '78': 42, '76': 40, '74': 38, '72': 36, '70': 34, '68': 32, '66': 30, '64': 28, '62': 26, '60': 24, '50': 22, '40': 20, '30': 18, '20': 16, '10': 14}, '3': {'100': 55, '95': 53, '90': 51, '85': 48, '80': 45, '78': 43, '76': 41, '74': 39, '72': 37, '70': 35, '68': 33, '66': 31, '64': 29, '62': 27, '60': 25, '50': 23, '40': 21, '30': 19, '20': 17, '10': 15}}, 'num'], '坐位体前屈': [{'1': {'100': 24.2, '95': 22.5, '90': 20.8, '85': 19.1, '80': 17.4, '78': 16.1, '76': 14.8, '74': 13.5, '72': 12.2, '70': 10.9, '68': 9.6, '66': 8.3, '64': 7.0, '62': 5.7, '60': 4.4, '50': 3.6, '40': 2.8, '30': 2.0, '20': 1.2, '10': 0.4}, '2': {'100': 24.8, '95': 23.1, '90': 21.4, '85': 19.7, '80': 18.0, '78': 16.7, '76': 15.4, '74': 14.1, '72': 12.8, '70': 11.5, '68': 10.2, '66': 8.9, '64': 7.6, '62': 6.3, '60': 5.0, '50': 4.2, '40': 3.4, '30': 2.6, '20': 1.8, '10': 1.0}, '3': {'100': 25.3, '95': 23.6, '90': 21.9, '85': 20.2, '80': 18.5, '78': 17.2, '76': 15.9, '74': 14.6, '72': 13.3, '70': 12.0, '68': 10.7, '66': 9.4, '64': 8.1, '62': 6.8, '60': 5.5, '50': 4.7, '40': 3.9, '30': 3.1, '20': 2.3, '10': 1.5}}, 'num'], '50米': [{'1': {'100': 7.8, '95': 7.9, '90': 8.0, '85': 8.3, '80': 8.6, '78': 8.8, '76': 9.0, '74': 9.2, '72': 9.4, '70': 9.6, '68': 9.8, '66': 10.0, '64': 10.2, '62': 10.4, '60': 10.6, '50': 10.8, '40': 11.0, '30': 11.2, '20': 11.4, '10': 11.6}, '2': {'100': 7.7, '95': 7.8, '90': 7.9, '85': 8.2, '80': 8.5, '78': 8.7, '76': 8.9, '74': 9.1, '72': 9.3, '70': 9.5, '68': 9.7, '66': 9.9, '64': 10.1, '62': 10.3, '60': 10.5, '50': 10.7, '40': 10.9, '30': 11.1, '20': 11.3, '10': 11.5}, '3': {'100': 7.6, '95': 7.7, '90': 7.8, '85': 8.1, '80': 8.4, '78': 8.6, '76': 8.8, '74': 9.0, '72': 9.2, '70': 9.4, '68': 9.6, '66': 9.8, '64': 10.0, '62': 10.2, '60': 10.4, '50': 10.6, '40': 10.8, '30': 11.0, '20': 11.2, '10': 11.4}}, 'time-short'], '800米': [{'1': {'100': '3\'24"', '95': '3\'30"', '90': '3\'36"', '85': '3\'43"', '80': '3\'50"', '78': '3\'55"', '76': '4\'00"', '74': '4\'05"', '72': '4\'10"', '70': '4\'15"', '68': '4\'20"', '66': '4\'25"', '64': '4\'30"', '62': '4\'35"', '60': '4\'40"', '50': '4\'50"', '40': '5\'00"', '30': '5\'10"', '20': '5\'20"', '10': '5\'30"'}, '2': {'100': '3\'22"', '95': '3\'28"', '90': '3\'34"', '85': '3\'41"', '80': '3\'48"', '78': '3\'53"', '76': '3\'58"', '74': '4\'03"', '72': '4\'08"', '70': '4\'13"', '68': '4\'18"', '66': '4\'23"', '64': '4\'28"', '62': '4\'33"', '60': '4\'38"', '50': '4\'48"', '40': '4\'58"', '30': '5\'08"', '20': '5\'18"', '10': '5\'28"'}, '3': {'100': '3\'20"', '95': '3\'26"', '90': '3\'32"', '85': '3\'39"', '80': '3\'46"', '78': '3\'51"', '76': '3\'56"', '74': '4\'01"', '72': '4\'06"', '70': '4\'11"', '68': '4\'16"', '66': '4\'21"', '64': '4\'26"', '62': '4\'31"', '60': '4\'36"', '50': '4\'46"', '40': '4\'56"', '30': '5\'06"', '20': '5\'16"', '10': '5\'26"'}}, 'time-long'], '肺活量': [{'1': {'100': 3150, '95': 3100, '90': 3050, '85': 2900, '80': 2750, '78': 2650, '76': 2550, '74': 2450, '72': 2350, '70': 2250, '68': 2150, '66': 2050, '64': 1950, '62': 1850, '60': 1750, '50': 1710, '40': 1670, '30': 1630, '20': 1590, '10': 1550}, '2': {'100': 3250, '95': 3200, '90': 3150, '85': 3000, '80': 2850, '78': 2750, '76': 2650, '74': 2550, '72': 2450, '70': 2350, '68': 2250, '66': 2150, '64': 2050, '62': 1950, '60': 1850, '50': 1810, '40': 1770, '30': 1730, '20': 1690, '10': 1650}, '3': {'100': 3350, '95': 3300, '90': 3250, '85': 3100, '80': 2950, '78': 2850, '76': 2750, '74': 2650, '72': 2550, '70': 2450, '68': 2350, '66': 2250, '64': 2150, '62': 2050, '60': 1950, '50': 1910, '40': 1870, '30': 1830, '20': 1790, '10': 1750}}, 'num']}}
    print("[SSS-CMD] 未检测到外置评分标准，已使用内置默认标准")

def time_format(time):
    time_temp = time.split("\'")
    time_temp[1] = time_temp[1].replace("\"", "")
    time = int(time_temp[0])*60 + int(time_temp[1])
    return time

def getScore(num, standard, type:str="num"):
    if type=="num":
        num = int(num)
        standard = {value: key for key, value in standard.items()}
    elif type=="time-long":
        num = time_format(num)
        standard = {value: key for key, value in standard.items()}
        standard = {value: time_format(str(key)) for key, value in standard.items()}
        standard = {value: int(key) for key, value in standard.items()}
    elif type=="time-short":
        num = int(float(num)*10)
        # print(standard)
        standard = {value: key for key, value in standard.items()}
        # print(standard)
        standard = {value: int(key*10) for key, value in standard.items()}
        # print(standard)
        standard = {value: int(key) for key, value in standard.items()}
        # print(standard)
    keys = list(standard.keys())
    ran = 0
    for k in standard:
        if type=="num":
            value = list(standard.values())
            if (num>keys[0]) : 
                return 100
            elif (num<keys[-1]) : 
                return 0
            ran += 1
            if num>=int(k):
                score = value[ran-1]
                break
        elif type=="time-long" or type=="time-short":
            # print(k , num)
            
            value = list(standard.values())[::-1]
            # print(value)
            if (num<keys[0]) : 
                return 100
            elif (num>keys[-1]) : 
                return 0
            ran += 1
            # print(num, k)
            if num<=float(k):
                # print(ran, value)
                score = value[-ran]
                break


    return score


if __name__ == "__main__":
    while True:
        try:
            userInput = input(f"[SSS-CMD] I.请输入需要评分的性别：\n[SSS-CMD] 提示：{Colors.BLUE}“b”：男{Colors.ENDC}，{Colors.RED}“g”：女{Colors.ENDC}，{Colors.BOLD}“f”或“F”或“Ctrl+Z”：退出程序{Colors.ENDC}\n[SSS-CMD] \t >>> ")
            if (userInput=="F" or userInput=="f"):
                print(f"\n[SSS-CMD] {Colors.BOLD}正在退出程序...{Colors.ENDC}")
                break
            elif (userInput=="b" or userInput=="g"):
                sexDict = {"b": ["男", f"{Colors.BLUE}男{Colors.ENDC}", "1:立定跳远; 2:引体向上; 3:坐位体前屈; 4:50米; 5:1000米; 6:肺活量"], "g": ["女", f"{Colors.RED}女{Colors.ENDC}", "1:立定跳远; 2:仰卧起坐; 3:坐位体前屈; 4:50米; 5:800米; 6:肺活量"]}
                sex = sexDict[userInput]
                print(f"[SSS-CMD] 你选择的性别是：{sex[1]}\n")

                while True:
                    userInput = input(f"[SSS-CMD] II.请输入年级（数字）：\n[SSS-CMD] 提示：{Colors.BOLD}“f”或“F”或“Ctrl+Z”：退出程序{Colors.ENDC}\n[SSS-CMD] \t >>> ")
                    if (userInput=="F" or userInput=="f"):
                        break
                    else:
                        grade = userInput
                    print(f"[SSS-CMD] 你选择的年级是：{Colors.BOLD}{grade}{Colors.ENDC}\n")

                    while True:
                        userInput = input(f"[SSS-CMD] III.请输入需要评分的项目（中文全称或数字）：\n[SSS-CMD] 提示：{Colors.BOLD}{sex[2]}{Colors.ENDC}，{Colors.BOLD}“f”或“F”或“Ctrl+Z”：退出程序{Colors.ENDC}\n[SSS-CMD] \t >>> ")
                        programDict = {"男": {1:"立定跳远", 2:"引体向上", 3:"坐位体前屈", 4:"50米", 5:"1000米", 6:"肺活量"}, "女": {1:"立定跳远", 2:"仰卧起坐", 3:"坐位体前屈", 4:"50米", 5:"800米", 6:"肺活量"}}
                        if (userInput=="F" or userInput=="f"):
                            break
                        elif (userInput.isdigit()):
                            program = programDict[sex[0]][int(userInput)]
                        else:
                            program = userInput
                        print(f"[SSS-CMD] 你选择的项目是：{Colors.BOLD}{program}{Colors.ENDC}\n")
                        
                        while True:
                            userInput = input(f"[SSS-CMD] IV.请输入数字或对应时间（长时间需用m\'s\"表示）：\n[SSS-CMD] 输入{Colors.BOLD}“f”或“F”或“Ctrl+Z”：退出程序{Colors.ENDC}\n[SSS-CMD] \t >>> ")
                            if (userInput=="F" or userInput=="f"):
                                break
                            else:
                                # print(sstandard[sex[0]][program][0][grade], sstandard[sex[0]][program][1])
                                # try: 
                                    
                                result = getScore(userInput, sstandard[sex[0]][program][0][grade], sstandard[sex[0]][program][1])
                                print(f"[SSS-CMD] {Colors.GREEN}计算成功!{Colors.ENDC}\n")
                                print(f"[SSS-CMD] {Colors.BOLD}结果为：{result}{Colors.ENDC}\n")
                                # except Exception as e:
                                #     print(f"[SSS-CMD] {Colors.RED}计算失败!{Colors.ENDC}\n")
                                #     print(f"[SSS-CMD] {Colors.BOLD}错误代码：{e}{Colors.ENDC}\n")
                    

            else:
                print(f"[SSS-CMD] {Colors.YELLOW}输入格式错误，请重新输入{Colors.ENDC}\n")
        except Exception as error:
            print(f"[SSS-CMD] {Colors.YELLOW}输入异常{Colors.ENDC}")
            input("[SSS-CMD] 按下回车键退出程序")
            # print(error)
            break
    
    