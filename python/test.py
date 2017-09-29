import pexpect
p = pexpect.spawn("/bin/cat")
p.send("123456789n")
p.expect(r"(345)..(.)")
print "Match1: " + p.before + '"' + p.after + '"'
print p.match.groups()
print p.match