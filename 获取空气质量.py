import requests
def gt(ip,op,i):
    f=op.find(ip)
    bi=f+len(ip)
    fi=bi+i
    val=op[bi:fi]
    return val

def main():
    inp=input('输入城市拼音(小写)：(退出请按q或Q)')
    while inp != 'q' and inp != 'Q':
        url='http://pm25.in/'+inp
        f = requests.get(url, timeout=10)
        if f.status_code != 200:
            print('网络断开')
        else:
            op = f.text
        aqis='''    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
        sys='''    <div class="span12 caution">
      <div class="primary_pollutant">
          <p>首要污染物：
            '''
        jys='''          </p>
      </div> <!-- end of .affect -->
      <div class="action">
          <p>建议采取的措施：
            '''
        citys='''<div class="span12 avg">
    <div class="span11">
      <div class="city_name">
          <h2>'''
        zhis='''</div> <!-- end of .city_name -->
      <div class="level">
          <h4>
            '''
        aqi=gt(aqis,op,2)
        sy=gt(sys,op,10)
        jy=gt(jys,op,35)
        city=gt(citys,op,4)
        zhi=gt(zhis,op,6)
        if sy[1]==' ':
            sy='无'
        if city[-1]=='/':
            city=city[:2]
        if city[-1]=='<':
            city=city[:3]
        
        kl=jy.split( )
        jy=kl[0]

        print('城市:{}，AQI为{}，空气质量:{}首要污染物:{}，建议:{}'.format(city,aqi,zhi,sy,jy))
        inp = input('输入城市拼音(小写)：(退出请按q或Q)')
    print('程序已退出')

if __name__ == '__main__':
    main()
