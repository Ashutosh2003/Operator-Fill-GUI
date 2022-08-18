import random

def gen_eqn(size,max_val,divisons):
    ops = ["+","+","-","-","*"]
    nums = []
    op_pos = [-1]
    eqn = ""

    for i in range(size):
        num = random.randint(1,max_val)
        nums.append(num)
        eqn = eqn + str(num)
        op_pos.append(len(eqn))
        eqn += ops[random.randint(0,len(ops)-1)]
    num = random.randint(1,max_val)
    nums.append(num)
    eqn = eqn + str(num)
    op_pos.append(len(eqn))

    #Division values generate
    div_factor = random.randint(1,10)
    if divisons == 1 and div_factor < 7:
        indx = -1
        ret = gen_division(eqn,op_pos,nums,indx)
        eqn = ret[0]
        op_pos = ret[1]
        nums = ret[2]
        indx = ret[3]
        for i in range(1,int(size/2)):
            ret = gen_division(eqn,op_pos,nums,indx)
            eqn = ret[0]
            op_pos = ret[1]
            nums = ret[2]
    
    ans = round(eval(eqn),3)
    eqn = eqn + " = " + str(ans)
    nums.append(ans)

    ret_val = ["",[]]
    ret_val[0] = eqn
    ret_val[1] = nums
    print(ret_val)
    return ret_val

           
def gen_division(eqn,op_pos,nums,indx):
    ops = ["+","-","*","/"]
    ret = ["",[],[],-1]
    index = random.randint(1,len(op_pos)-2)
    if index == indx+1 or index == indx-1:
        ret[0] = eqn
        ret[1] = op_pos
        ret[2] = nums
        return ret
                
    divisor = random.randint(1,10)
    dividend = int(divisor*0.5*random.randint(2,20))
    nums[index-1],nums[index] = dividend,divisor
    div_str = str(dividend) + "/" + str(divisor)

    replace_str = eqn[op_pos[index-1]+1:op_pos[index+1]]
    eqn = eqn.replace(replace_str,div_str,1)

    op_pos = [-1]
    for i in range(len(eqn)):
        if eqn[i] in ops:
            op_pos.append(i)
    op_pos.append(len(eqn))

    pos = op_pos[index]

    ret[0] = eqn
    ret[1] = op_pos
    ret[2] = nums
    ret[3] = index

    return ret


#print(div_str,replace_str)
#print(op_pos,eqn,index,eqn2,op_pos2)
