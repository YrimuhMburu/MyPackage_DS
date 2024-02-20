from MyPackage import MyModule
def test_top_n():
     """
     ensuring top_n works properly
     """
#using assert to test the function 
assert MyModule.top_n([10,3,6,8,5],4)== [10,8,6], 'incorrect'
assert MyModule.top_n([90,30,69,8],3)== [90,69,30], 'incorrect'
assert MyModule.top_n([100,45,6,76,54],4)== [100,76,54,45], 'incorrect'