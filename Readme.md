**iApp BVT自动化测试程序（Python版）**
运行环境：
- appium server
- python3
- unittest, pytest
- git

配置文件：iAppBVT_Python.json
- 将配置文件复制到本地磁盘
- 填入设备的 deviceName 与 udid

运行命令：
pytest -sv test/bvt_test.py --tc-file /full path/iAppBVT_Python.json --tc-format json