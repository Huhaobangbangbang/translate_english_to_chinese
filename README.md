# translate_english_to_chinese
We have two choice.One is multi-threaded, the other is free single-threaded provided by baidu



# Add a environment variable
 export BAIDU_TRANSLATE_API_AUTH="./baidu_translate/auth.json"
The auth-file contains your service account key.

Example:

{
    "APPID": "XXXXX",
    "SECRETKEY": "XXXX",
    "SERVER": "api.fanyi.baidu.com"
}


# You need to register on http://api.fanyi.baidu.com/product/112 to get APPID and SECRETKEY
参考链接： https://github.com/mymusise/Baidu-Translation-SDK
