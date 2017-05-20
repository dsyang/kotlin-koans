from __future__ import absolute_import
import sys
sys.path.insert(0, "/Users/dsyang/buck/third-party/py/pathlib")
sys.path.insert(0, "/Users/dsyang/buck/third-party/py/pywatchman")
sys.path.insert(0, "/Users/dsyang/buck/third-party/py/typing/python2")
sys.path.insert(0, "/Users/dsyang/buck/build/classes")
sys.path.insert(0, "/Users/dsyang/Sandbox/kotlin-koans/.buckd/tmp/buck_run.nMPHxr/buck_python_program4846632818637819956")
if __name__ == '__main__':
    try:
        from buck_parser import buck
        buck.main()
    except KeyboardInterrupt:
        print >> sys.stderr, 'Killed by User'
