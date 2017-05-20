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
        java = ""
        number = ds.split('_')[1]
        if len([x for x in os.listdir(ds) if x.endswith(".java")]) > 0:
            print "java present in %s" % ds
            java = """java_library(
    name = "java",
    srcs = glob(["*.java"]),
    deps = [
        "//src/util:util-java",
    ],
    exported_deps = [
        "//src/util:util-java",
    ],
    visibility = [
        "//src/i_introduction/%s:%s",
    ]
)
""" % (ds, number)
        kotlin = """kotlin_library(
    name = "%s",
    srcs = glob(["*.kt"]),
    tests = [
        "//test/i_introduction/%s:%s",
    ],
    deps = [
        "//src/util:util-kotlin",
    ],
    visibility = ["PUBLIC"],
)
""" % (number, ds, number)
        output["%s/BUCK" % ds] = "%s%s" % (kotlin, java)

for k,v in output.items():
    with open(k, "w") as f:
        f.write(v)
