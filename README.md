# ๐ฐ ๅ่ดฃ็ณๆ
ๆฌ็จๅบไปไพๆๆๅฎๅจๆต่ฏๅไธชไบบๅญฆไน ไฝฟ็จ๏ผ่ฏทๅฟๅฉ็จ็จๅบไธญ็ๆปๅปไปฃ็ ไปไบ้ๆณๆต่ฏใ็ฑไบไผ ๆญใๅฉ็จ็จๅบไธญๆๆไพ็ๆปๅปไปฃ็ ่้ ๆ็ไปปไฝ็ดๆฅๆ่้ดๆฅ็ๅๆๅๆๅคฑ๏ผๅ็ฑไฝฟ็จ่ๆฌไบบ่ด่ดฃ๏ผ็จๅบไฝ่ไธไธบๆญคๆฟๆไปปไฝ่ดฃไปปใ

# SecTools
๐ Powered by Norah C.IV

## ๐ Tree
```
.
โโโ LICENSE
โโโ main.py
โโโ pocsuite3
โย ย  โโโ api
โย ย  โย ย  โโโ __init__.py
โย ย  โโโ brute
โย ย  โย ย  โโโ ftp_burst.py
โย ย  โย ย  โโโ ldap_burst.py
โย ย  โย ย  โโโ memcache_burst.py
โย ย  โย ย  โโโ mongodb_burst.py
โย ย  โย ย  โโโ mssql_burst.py
โย ย  โย ย  โโโ mysql_burst.py
โย ย  โย ย  โโโ postgresql_burst.py
โย ย  โย ย  โโโ redis_burst.py
โย ย  โย ย  โโโ ssh_burst.py
โย ย  โย ย  โโโ telnet_burst.py
โย ย  โย ย  โโโ vnc_burst.py
โย ย  โโโ cli.py
โย ย  โโโ console.py
โย ย  โโโ data
โย ย  โย ย  โโโ dic_password_ftp.txt
โย ย  โย ย  โโโ dic_password_imap_ssl.txt
โย ย  โย ย  โโโ dic_password_imap.txt
โย ย  โย ย  โโโ dic_password_memcached.txt
โย ย  โย ย  โโโ dic_password_mongodb.txt
โย ย  โย ย  โโโ dic_password_mysql.txt
โย ย  โย ย  โโโ dic_password_oracle.txt
โย ย  โย ย  โโโ dic_password_pop3.txt
โย ย  โย ย  โโโ dic_password_postgresql.txt
โย ย  โย ย  โโโ dic_password_rdp.txt
โย ย  โย ย  โโโ dic_password_redis.txt
โย ย  โย ย  โโโ dic_password_smb.txt
โย ย  โย ย  โโโ dic_password_smtp.txt
โย ย  โย ย  โโโ dic_password_sqlserver.txt
โย ย  โย ย  โโโ dic_password_ssh.txt
โย ย  โย ย  โโโ dic_password_svn.txt
โย ย  โย ย  โโโ dic_password_telnet.txt
โย ย  โย ย  โโโ dic_password_tomcat.txt
โย ย  โย ย  โโโ dic_password_vnc.txt
โย ย  โย ย  โโโ dic_password_weblogic.txt
โย ย  โย ย  โโโ dic_username_ftp.txt
โย ย  โย ย  โโโ dic_username_imap.txt
โย ย  โย ย  โโโ dic_username_memcached.txt
โย ย  โย ย  โโโ dic_username_mongodb.txt
โย ย  โย ย  โโโ dic_username_mysql.txt
โย ย  โย ย  โโโ dic_username_oracle.txt
โย ย  โย ย  โโโ dic_username_pop3.txt
โย ย  โย ย  โโโ dic_username_postgresql.txt
โย ย  โย ย  โโโ dic_username_rdp.txt
โย ย  โย ย  โโโ dic_username_redis.txt
โย ย  โย ย  โโโ dic_username_smb.txt
โย ย  โย ย  โโโ dic_username_smtp.txt
โย ย  โย ย  โโโ dic_username_sqlserver.txt
โย ย  โย ย  โโโ dic_username_ssh.txt
โย ย  โย ย  โโโ dic_username_svn.txt
โย ย  โย ย  โโโ dic_username_telnet.txt
โย ย  โย ย  โโโ dic_username_tomcat.txt
โย ย  โย ย  โโโ dic_username_vnc.txt
โย ย  โย ย  โโโ dic_username_weblogic.txt
โย ย  โโโ __init__.py
โย ย  โโโ lib
โย ย  โย ย  โโโ controller
โย ย  โย ย  โย ย  โโโ controller.py
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ core
โย ย  โย ย  โย ย  โโโ clear.py
โย ย  โย ย  โย ย  โโโ common.py
โย ย  โย ย  โย ย  โโโ convert.py
โย ย  โย ย  โย ย  โโโ data.py
โย ย  โย ย  โย ย  โโโ datatype.py
โย ย  โย ย  โย ย  โโโ decorators.py
โย ย  โย ย  โย ย  โโโ enums.py
โย ย  โย ย  โย ย  โโโ exception.py
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โโโ interpreter_option.py
โย ย  โย ย  โย ย  โโโ interpreter.py
โย ย  โย ย  โย ย  โโโ log.py
โย ย  โย ย  โย ย  โโโ optiondict.py
โย ย  โย ย  โย ย  โโโ option.py
โย ย  โย ย  โย ย  โโโ plugin.py
โย ย  โย ย  โย ย  โโโ poc.py
โย ย  โย ย  โย ย  โโโ readlineng.py
โย ย  โย ย  โย ย  โโโ register.py
โย ย  โย ย  โย ย  โโโ revision.py
โย ย  โย ย  โย ย  โโโ settings.py
โย ย  โย ย  โย ย  โโโ shell.py
โย ย  โย ย  โย ย  โโโ statistics_comparison.py
โย ย  โย ย  โย ย  โโโ threads.py
โย ย  โย ย  โย ย  โโโ update.py
โย ย  โย ย  โโโ helper
โย ย  โย ย  โย ย  โโโ archieve
โย ย  โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โย ย  โโโ jar.py
โย ย  โย ย  โย ย  โย ย  โโโ memoryzip.py
โย ย  โย ย  โย ย  โย ย  โโโ war.py
โย ย  โย ย  โย ย  โย ย  โโโ zip.py
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โโโ java
โย ย  โย ย  โย ย      โโโ __init__.py
โย ย  โย ย  โย ย      โโโ serialization.py
โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ parse
โย ย  โย ย  โย ย  โโโ cmd.py
โย ย  โย ย  โย ย  โโโ configfile.py
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โโโ rules.py
โย ย  โย ย  โย ย  โโโ url.py
โย ย  โย ย  โโโ request
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โโโ patch
โย ย  โย ย  โย ย      โโโ add_httpraw.py
โย ย  โย ย  โย ย      โโโ hook_request.py
โย ย  โย ย  โย ย      โโโ hook_request_redirect.py
โย ย  โย ย  โย ย      โโโ hook_urllib3_parse_url.py
โย ย  โย ย  โย ย      โโโ __init__.py
โย ย  โย ย  โย ย      โโโ remove_ssl_verify.py
โย ย  โย ย  โย ย      โโโ remove_warnings.py
โย ย  โย ย  โย ย      โโโ unquote_request_uri.py
โย ย  โย ย  โโโ utils
โย ย  โย ย      โโโ __init__.py
โย ย  โย ย      โโโ markup.py
โย ย  โย ย      โโโ pcap_sniffer.py
โย ย  โโโ modules
โย ย  โย ย  โโโ censys
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ ceye
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ fofa
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ httpserver
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ interactsh
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ listener
โย ย  โย ย  โย ย  โโโ bind_tcp.py
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โย ย  โโโ reverse_tcp.py
โย ย  โย ย  โโโ quake
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ seebug
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ shodan
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ spider
โย ย  โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ zoomeye
โย ย  โย ย      โโโ __init__.py
โย ย  โโโ plugins
โย ย  โย ย  โโโ file_record.py
โย ย  โย ย  โโโ html_report.py
โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ poc_from_pocs.py
โย ย  โย ย  โโโ poc_from_redis.py
โย ย  โย ย  โโโ poc_from_seebug.py
โย ย  โย ย  โโโ target_from_censys.py
โย ย  โย ย  โโโ target_from_cidr.py
โย ย  โย ย  โโโ target_from_fofa.py
โย ย  โย ย  โโโ target_from_quake.py
โย ย  โย ย  โโโ target_from_redis.py
โย ย  โย ย  โโโ target_from_shodan.py
โย ย  โย ย  โโโ target_from_zoomeye.py
โย ย  โโโ pocs
โย ย  โย ย  โโโ __init__.py
โย ย  โย ย  โโโ jboss_cve_2015_7501_unserialization.py
โย ย  โย ย  โโโ redis_unauthorized_access.py
โย ย  โย ย  โโโ sunlogin_rce.py
โย ย  โย ย  โโโ zookeeper_unauthorized_access.py
โย ย  โโโ shellcodes
โย ย      โโโ base.py
โย ย      โโโ data
โย ย      โย ย  โโโ java
โย ย      โย ย  โย ย  โโโ src
โย ย      โย ย  โย ย      โโโ ReverseTCP
โย ย      โย ย  โย ย          โโโ Payload.java
โย ย      โย ย  โโโ linux
โย ย      โย ย  โย ย  โโโ bind_tcp.bin
โย ย      โย ย  โย ย  โโโ reverse_tcp.bin
โย ย      โย ย  โย ย  โโโ src
โย ย      โย ย  โย ย  โย ย  โโโ bind_tcp.asm
โย ย      โย ย  โย ย  โย ย  โโโ reverse_tcp.asm
โย ย      โย ย  โย ย  โโโ x64
โย ย      โย ย  โย ย      โโโ bind_tcp.bin
โย ย      โย ย  โย ย      โโโ reverse_tcp.bin
โย ย      โย ย  โย ย      โโโ src
โย ย      โย ย  โย ย          โโโ bind_tcp.asm
โย ย      โย ย  โย ย          โโโ reverse_tcp.asm
โย ย      โย ย  โโโ windows
โย ย      โย ย      โโโ bind_tcp.bin
โย ย      โย ย      โโโ reverse_tcp.bin
โย ย      โย ย      โโโ src
โย ย      โย ย      โย ย  โโโ bind_tcp.asm
โย ย      โย ย      โย ย  โโโ reverse_tcp.asm
โย ย      โย ย      โโโ x64
โย ย      โย ย          โโโ bind_tcp.bin
โย ย      โย ย          โโโ reverse_tcp.bin
โย ย      โย ย          โโโ src
โย ย      โย ย              โโโ bind_tcp.asm
โย ย      โย ย              โโโ reverse_tcp.asm
โย ย      โโโ dotnet.py
โย ย      โโโ encoder.py
โย ย      โโโ generator.py
โย ย      โโโ __init__.py
โย ย      โโโ java.py
โย ย      โโโ php.py
โย ย      โโโ python.py
โโโ README.md
โโโ requirements.txt
โโโ scan_func
โย ย  โโโ github.py
โย ย  โโโ passwdscan.py
โย ย  โโโ portscan.py
โย ย  โโโ vulscan.py
โโโ scan_github
โย ย  โโโ monitor.py
โโโ scan_port
โย ย  โโโ scan.py
โโโ scan_result
โย ย  โโโ __init__.py
โโโ scan_start
โย ย  โโโ format_table.py
โย ย  โโโ get_file.py
โย ย  โโโ start.py
โโโ sec_img
    โโโ github.png
    โโโ port_scan.png
    โโโ portscan.png
    โโโ redis_scan.png
    โโโ spider_2.jpg
    โโโ spider.jpg
    โโโ start.png
    โโโ vulscan_1.png
    โโโ vulscan_2.png
    โโโ vulscan.png
    โโโ weakpass.png
```

## ๐ฅ ไฝฟ็จๅงฟๅฟ
`python main.py`

![start.png](sec_img/start.png)

## ๐ฅ Function
### โจ ๆผๆดๆซๆ
![vulscan.png](sec_img/vulscan.png)
๐ค ไฝฟ็จๆชๅพ
![vulscan_1.png](sec_img/vulscan_1.png)
![vulscan_2.png](sec_img/vulscan_2.png)

### โจ ็ซฏๅฃๆซๆ
๐ค ไฝฟ็จๆชๅพ
![portscan.png](sec_img/portscan.png)

### โจ ๅผฑๅฃไปคๆปๅป
(็ฎๅๅทฎpostgresqlใvncใldap๏ผๅซ้ฎไธบไปไนๆฒกๅ๏ผ้ฎๅฐฑๆฏไธไผ)
![weakpass.png](sec_img/weakpass.png)
๐ค ไฝฟ็จๆชๅพ
![redis_scan.png](sec_img/redis_scan.png)

### โจ Github็ฌ่ซ
(็ฝ็ป้ฎ้ขไผ้ข็นๆฅ้๏ผๆชๅ ไปฃ็๏ผ็ญๆๅญฆไน ๅฎไฝฟ็จ็ณป็ปไปฃ็ๅไฟฎๆนไปฃ็ )
๐ค ไฝฟ็จๆชๅพ
![spider.jpg](sec_img/spider.jpg)
![spider_2.jpg](sec_img/spider_2.jpg)

# ๐ ๆถๅ้กน็ฎ
[pocsuite3](https://github.com/knownsec/pocsuite3)

[POC-bomber](https://github.com/tr0uble-mAker/POC-bomber)

# ๐ TODO
(SecTools v2.0่งๅ)
- POCๅ็ฑป๏ผๅนถๅ ๅฅๆน้ๆซๆ
- ไผๅๅๆณ๏ผ้ฟๅไปฃ็ ้ๅค
- ๅขๅ ๅญๅๆขๆตใ่ทฏๅพๆขๆต็ญๅธธ็จๅ่ฝ
- ๅขๅ GitHub Code้จๅ็ฌๅ
- ๅขๅ POCๆ็ดขๅ่ฝ