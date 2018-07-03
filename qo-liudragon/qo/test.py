testset = dict()
testset['a'] = 'b'
set2 = dict()
set2['b'] = 'c'
testset['b'] = set2
if testset['b']:
    print 'b'
if testset:
    print 'a'