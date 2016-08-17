from PicInWord import PicInWord

'''
extract images from filename you
specify into the directory
you want to store these images
'''

test=PicInWord()

print "please input the destination of file"
filename=raw_input()
filename=filename.replace('\\',"/")
print filename

print "please input the directory to store the pictures obtained from your file"
outdir=raw_input()
outdir=outdir.replace('\\',"/")
print outdir
test.extract_image(filename,outdir)

