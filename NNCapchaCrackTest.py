from PIL import Image
# img = Image.open("input/input00.jpg")


dr=40
dg=40
db=40

fileName=''
loop=0
for loop in range(25):
    x1 = 1000
    x2 = -1
    y1 = 1000
    y2 = -1
    fileName =  str(loop)
    if(loop<10):
        fileName='0'+str(loop)
    im=""
    im = Image.open('input/input'+fileName+'.jpg') # Can be many different formats.
    pix = im.load()
    # print im.size


    for px in range(im.size[0]):
        for py in range(im.size[1]):

            if(( pix[px,py][0]>db ) &( pix[px,py][0]>dg ) & ( pix[px,py][0]>dr )):
                pix[px, py] = 255,255,255

            else:
                pix[px, py] = 0, 0, 0
                # conternt part axsis find
                if (px < x1): x1 = px
                if (px > x2): x2 = px
                if (py < y1): y1 = py
                if (py > y2): y2 = py


            # print pix[px, py];
    # print x1, x2,y1,y2;
    print 'x1:' + str(x1) + '/x2:' + str(x2) + '/y1:' + str(y1) + '/y2:' + str(y2);


    xx1=x1;
    yy1=y1;
    count = 0
    isNestedEmptyHas=1
    for px in range(x1,x2):
        empty=1

        for py in range(y1,y2):
            # print 'x'+str(px)+'/y'+str(py);
            if( pix[px, py][0] ==0):
                empty=0
                if(px<xx1):xx1=px
                isNestedEmptyHas=0


        if((empty==1) & (isNestedEmptyHas==0)):
            print "=>>"+str(xx1)+","+str(y1)+"/"+str(px-1)+","+str(y2)

            # yy1=py
            left = xx1
            top = y1
            width = 8
            height = 10
            box = (left, top, left + width, top + height)


            area = im.crop(box)

            area.save('inputCrop/input' + fileName + "_"+str(count)+'.png')
            xx1=1000
            isNestedEmptyHas = 1
            count=count+1

    print "=>>"+str(xx1)+","+str(y1)+"/"+str(x2)+","+str(y2)



    # ========================================
    left = xx1
    top = y1
    width = 8
    height = 10
    box = (left, top, left + width, top + height)
    
    # print box;

    area = im.crop(box)
    # print area;
    area.save('inputCrop/input' + fileName + "_" + str(count) + '.png')

    im.save('inputMod/input'+fileName+'.png')  # Save the modified pixels as .png

