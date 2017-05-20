import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

print os.path.abspath(".")
output = {}
for ds in os.listdir("."):
    if "BUCK" not in os.listdir(ds):
        number = ds.split('_')[1]
        kotlin = """kotlin_test(
    name = "%s",
    srcs = glob(["*.kt"]),
    deps = [
        "//src/i_introduction/%s:%s",
        "//lib:junit",
    ],
    visibility = ["PUBLIC"],
)
""" % (number, ds, number)
        output["%s/BUCK" % ds] = "%s" % (kotlin)

for k,v in output.items():
#    print k
#    print v
    with open(k, "w") as f:
        f.write(v)
