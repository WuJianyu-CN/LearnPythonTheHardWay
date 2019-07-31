'''
Write a function of my own design and run it 10 different ways
'''


def study(status, together):
    print(f"study {status} together with {together}")


study('hard', "Jay")
status = 'hard'
together = "jay"
study(status, 'Jay')
study(status+'1', 'Lily')
study(status, 'Lily ' + 'Jay')
study("hardly" + "hard", "Lily" + "jay" )
study(status, together)
study(status + ' hard',together + ' Lily')


status1 = input("intput status:\n > ")
together1 = input("input together:\n >")
study(status1, "jay")
study("hard", together1)
study(status1, together1)



