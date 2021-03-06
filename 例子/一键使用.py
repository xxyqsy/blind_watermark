# encoding:utf-8

from PIL import Image
import piexif
import os
import os
import subprocess
import os
import shutil

from blind_watermark import WaterMark

def get_value(value_get,str_info):
   
    attempts = 0
    success = False
    while attempts < 30000 and not success:
        try:
            
            value = int(input(str_info+"\n"))
            success = True
        except:
            print("输入错误请重新输入")
            attempts += 1
            if attempts == 3000:
                break
    return value
def get_str(str_get,str_info):
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            
            str_get = str(input(str_info+"\n"))
            success = True
        except:
            print("输入错误请重新输入"+str_info)
            attempts += 1
            if attempts == 3000:
                break
    return str_get

def mod_00():
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            yuantu_name_head = "abc"
            yuantu_name_head = get_str(yuantu_name_head,"输入你的原图文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            source = './yuantu/'+yuantu_name_head
            target = './shuchu/233313213.jpg'
            
            shu_liang = 50
            shu_liang = get_value(shu_liang,"输入你想生成的图片数量，数量无限制！")
            i = 1
            int(i)
            int(shu_liang)
            while i < shu_liang+1:
                ge_shi = str('.png') 
                



                source_in_loop = source
                target_in_loop = './shuchu/out_'+str(i)+"_"+yuantu_name_head

                print(target)
                print(source)
                shutil.copy(source, target_in_loop) 
                print("复制完成")
                cmd = ".\exiftool  -artist="+str(i)+" " + target_in_loop
                print(cmd)
                r1 = os.popen(cmd)
                print(r1.read())
                print(str(i/shu_liang*100)+"%已经完成")
                i =i+ 1
    
            input("复制完成")   
                
                                
                            
        except:
            print("程序出错，可能是你输入的文件名称错误,,请从头开始")
            attempts += 1
            if attempts == 3000:
                break
    return 0
def mod_01():
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            print("EXFI_图片水印解密模式：")
            print("请将你需要解密文件放置于jiemi文件夹下")
            jiemi_name = "abc"
            jiemi_name = get_str(jiemi_name,"输入你想要解密的文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            jiemi_name = 'jiemi/'+jiemi_name
            print("正在寻找"+jiemi_name+"待解密文件")
            cmd = ".\exiftool  -artist"+" " + jiemi_name
            #print(cmd)
            r1 = os.popen(cmd)
                
            print("解密信息如下，如为空，则此图无水印，数字为其序号")
            print(r1.read())
        except:
            print("程序出错，可能是你输入文件名称错误,,请从头开始")
            attempts += 1
            if attempts == 3000:
                break
    return 0
def mod_1():
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            print("默认工作模式：")
            password_wm = 123
            password_img = 123
            password_wm = get_value(password_wm,"请输入水印加密密码，只能是数字组合")
            password_img = get_value(password_img,"请输入原图加密密码，只能是数字组合")
            bwm1 = WaterMark(password_wm, password_img)
            print("请将你的原图放置于yuantu文件夹下")
            yuantu_name_head = "abc"
            yuantu_name_head = get_str(yuantu_name_head,"输入你的原图文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            yuantu_name = 'yuantu/'+yuantu_name_head
            print("正在寻找"+yuantu_name+"文件")
            bwm1.read_img(yuantu_name)
            print("图片已经被读取")
            shu_liang = 50
            shu_liang = get_value(shu_liang,"输入你想生成的图片数量，目前最大支持60张，\n 你可以自行放入wm_61/wm_62...，然后输入数量即可")
            i = 1
            int(i)
            int(shu_liang)
            while i < shu_liang+1:
                    ge_shi = str('.png') 
                    shuiyin_tu = str('shuiyin/wm_')
                    shuiyin_name = shuiyin_tu+str(i)+ge_shi
                    shuchu_tu = str('shuchu/img_')
                    shuchu_name = shuchu_tu+str(i)+"_"+yuantu_name_head
                    str(shuiyin_name)
                    str(shuchu_name)
                    print(shuiyin_name+"水印读取中")
                    print(shuchu_name+"输出图生成中")
                    
                    bwm1.read_wm(shuiyin_name)

                    bwm1.embed(shuchu_name)
                    print(str(i/shu_liang*100)+"%已经完成")
                    i =i+ 1
                    
                            
        except:
            print("程序出错，可能是你输入的图片过小，没有足够空间添加水印，或输入文件名称错误,,请从头开始")
            attempts += 1
            if attempts == 3000:
                break
    return 0
def mod_2():
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            print("自定义工作模式：")
            print("提示：此模式可以添加任意水印到任意图中，请注意本程序限制了水印的大小\n 以防止过大水印造成的画质损失，水印推荐使用透明底黑色标记符号或高反差图像，\n 原图越大，你可以写入的水印就越大，对于更大的图片，建议放置白底黑色二维码，\n 如果程序窗口出错，请注意出错内容中，可容纳大小提示")
            password_wm = 123
            password_img = 123
            password_wm = get_value(password_wm,"请输入水印加密密码，只能是数字组合")
            password_img = get_value(password_img,"请输入原图加密密码，只能是数字组合")
            bwm1 = WaterMark(password_wm, password_img)
            print("请将你的原图放置于yuantu文件夹下")
            yuantu_name = "abc"
            yuantu_name = get_str(yuantu_name,"输入你的原图文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            yuantu_name = 'yuantu/'+yuantu_name
            print("正在寻找"+yuantu_name+"原图文件")
            bwm1.read_img(yuantu_name)
            shuiyin_name = "abc"
            shuiyin_name = get_str(shuiyin_name,"输入你的水印文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            shuiyin_name = 'shuiyin/'+shuiyin_name
            print("正在寻找"+shuiyin_name+"水印文件")	
            bwm1.read_wm(shuiyin_name)
            shuchu_name = "abc"
            shuchu_name = get_str(shuchu_name,"输入你想要的输出文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            shuchu_name = 'shuchu/'+shuchu_name
            print("正在输出"+shuchu_name+"已加水印文件,请等待结束提示")
            bwm1.embed(shuchu_name)
            print("输出完毕\n\n\n\n")
                    
                            
        except:
            print("程序出错，可能是你输入的图片过小，没有足够空间添加水印，或输入文件名称错误,请从头开始")
            attempts += 1
            if attempts == 3000:
                break
    return 0
def mod_3():
   
    attempts = 0
    success = False
    while attempts < 3000 and not success:
        try:
            print("图片水印解密模式：")
            print("请将你需要解密文件放置于jiemi文件夹下")
            jiemi_name = "abc"
            jiemi_name = get_str(jiemi_name,"输入你想要解密的文件名,要带后缀,例如：abc.png/abc.jpg|不支持带汉字文件名")
            jiemi_name = 'jiemi/'+jiemi_name
            print("正在寻找"+jiemi_name+"待解密文件")
            password_wm = 123
            password_img = 123
            password_wm = get_value(password_wm,"请输入水印加密密码，只能是数字组合")
            password_img = get_value(password_img,"请输入原图加密密码，只能是数字组合")
            bwm1 = WaterMark(password_wm, password_img)
            print("请输入你曾经对这张图加的水印尺寸：例如如果你的水印是640 x 480的，则它的长是640，宽是480，如果是使用默认水印，请两次输入100 \n")
            x = 0
            y = 0 
            x = get_value(x,"请输入长:")
            y = get_value(y,"请输入宽:")
            print("你输入的长宽是%dx%d"%(x,y))
            print("正在运行。请等待结束提示")
            
            bwm1.extract(filename=jiemi_name, wm_shape=(x, y), out_wm_name='shuchu/jiemi.png', )	
            print("解密数据已经输出到shuichu文件夹下，名称为jiemi.png\n\n\n\n")
                    
                            
        except:
            print("程序出错，可能是输入文件名称或水印参数错误,,请从头开始")
            attempts += 1
            if attempts == 3000:
                break
    return 0






print("开发者：evenif/风栖木兮")
print("开源代码地址：https://github.com/guofei9987/blind_watermark")
print("本程序免费提供使用！")
print("程序开始运行：")
print("使用本程序前，请先运行一次本文件夹下的exiftool.exe，\n 本程序调用其对exif信息进行读写")
print("如程序出错，请检查你的输入内容，重新打开此程序即可")
print("请注意，本程序需要和其下文件夹配合工作他们分别是:\n yuantu:放置原图\n shuiyin；存放水印\n jiemi存放等待解密文件\n shuichu输出文件夹\n 复制此程序时，请直接打包本程序所在文件夹")

#选择工作核心
print("请选择程序工作内核：\n 1: Exif水印模式（不损失画质仅可查原画） \n 2: 盲水印模式（增加噪点，截图可查）")
core_mode = 0
core_mode=get_value(core_mode,"请选输入工作内核序号")
if core_mode != 0 and core_mode != 1 and  core_mode != 2:
    print("你输入的核心序号不存在")
    
if core_mode == 0:
    print("核心选择，错误次数过多，已关闭")
if core_mode == 1:
    print("已选择EXIF水印模式")
    print("请选择程序工作模式：\n 1: 默认工作模式\n \n 2: 水印解密模式")
    work_mode = 0
    work_mode=get_value(work_mode,"请选输入工作模式序号")
    if work_mode != 1 and work_mode != 1 and work_mode != 2 :
        print("你输入的工作模式序号不存在")
    if work_mode == 1 :    
        res = 1
        res = mod_00()
    if work_mode == 2 :
        res = 1
        res = mod_01()



if core_mode ==2:
    #选择工作模式
    print("已选择盲水印模式")
    print("请选择程序工作模式：\n 1: 默认工作模式（自动添加一定数量水印）\n 2: 自定义模式（请在文件夹添加你的自定义水印）\n 3: 水印解密模式（需要输入密码）")
    work_mode = 0
    work_mode=get_value(work_mode,"请选输入工作模式序号")
    if work_mode != 0 and work_mode != 1 and work_mode != 2 and work_mode != 3:
        print("你输入的工作模式序号不存在")
    if work_mode == 0:
        print("错误次数过多，已关闭")
    if work_mode == 1:
            res = 1 
            res = mod_1()
            
            

    if work_mode == 2:
            res = 1 
            res = mod_2()
    if work_mode == 3:
            res = 1 
            res = mod_3()

input("程序运行完毕，需要再次使用请重新打开")



