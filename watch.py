import datetime
import time

def clear():
  import os
  os.system("CLS")

dictionary = {
"0":
    """
    ■■■■■
    ■   ■
    ■   ■
    ■   ■
    ■■■■■""",
"1":
    """
      ■  
     ■■  
    ■ ■  
      ■  
    ■■■■■""",
"2":
    """
    ■■■■■
    ■   ■
      ■  
    ■    
    ■■■■■""",
"3":
    """
    ■■■■ 
        ■
      ■  
        ■
    ■■■■ """,
"4":
    """
    ■   ■
    ■   ■
    ■ ■ ■
        ■
        ■""",
"5":
    """
    ■■■■■
    ■    
    ■ ■ ■
        ■
    ■■■■■""",
"6":
    """
    ■■■■■
    ■    
    ■ ■ ■
    ■   ■
    ■■■■■""",
"7":
    """
    ■■■■■
        ■
      ■  
      ■  
      ■  """,
"8":
    """
    ■■■■■
    ■   ■
    ■■■■■
    ■   ■
    ■■■■■""",
"9":
    """
    ■■■■■
    ■   ■
    ■ ■ ■
        ■
    ■■■■■""",
":":
    """
         
      ■  
         
      ■  
         """,
" ":
    """
         
         
         
         
         """

}

while True:
    now = datetime.datetime.now()
    timestr = now.strftime("%H:%M:%S")

    a = dictionary[timestr[0]]
    b = dictionary[timestr[1]]
    c = dictionary[timestr[2]]
    d = dictionary[timestr[3]]
    e = dictionary[timestr[4]]
    f = dictionary[timestr[5]]
    g = dictionary[timestr[6]]
    h = dictionary[timestr[7]]

    a_lin = a.splitlines()
    b_lin = b.splitlines()
    c_lin = c.splitlines()
    c_p_lin = dictionary[" "].splitlines()
    d_lin = d.splitlines()
    e_lin = e.splitlines()
    f_lin = f.splitlines()
    f_p_lin = dictionary[" "].splitlines()
    g_lin = g.splitlines()
    h_lin = h.splitlines()

    def watch():
        if now.second % 2 == 0:
            for i in range(len(a_lin)):
                print(a_lin[i], b_lin[i], c_lin[i], d_lin[i], e_lin[i], f_lin[i], g_lin[i], h_lin[i])
        else:
            for i in range(len(a_lin)):
                print(a_lin[i], b_lin[i], c_p_lin[i], d_lin[i], e_lin[i], f_p_lin[i], g_lin[i], h_lin[i])
        print()    
  
  
    watch()             
    time.sleep(1)   
    clear()
 
