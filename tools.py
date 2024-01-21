import sys
import importlib
tool = sys.argv[1]

module = importlib.import_module(f"tools.{tool}", package="tools")
module.main()