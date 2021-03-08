# RERADME #

## Tradegecko

This project developed with Python3.65+ Django for Backend and Angular7.0 for Frontend
+ Dashboard
+ User management
+ Product(variant) management
+ Sku management
+ Media management using cloudinary
+ Order management
+ Sync products and other info with shopify, Magento, zudello, zapier, amazon, quickbooks

#### Preview
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img1.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img2.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img3.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img4.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img5.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img6.PNG)
![Relevance feedback image](https://github.com/certainty15750/tradegecko/blob/master/Screenshots/img7.PNG)


## SERVER ENVIRONMENT SETUP (Ubuntu18.04)
Here I described way to deploy to VPS server manually

 + Frontend(Angular7.0)
    + node
        + `curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -`
        + `sudo yum install nodejs`
    + npm
        + `npm install`
        + `npm start`
 + Backend(Django2.13)
    + python
        + `sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm`
        + `sudo yum -y install python36u`
        + `python3.6 -V`
    + pip
        + `sudo yum -y install python36u-pip`
        + `pip3.6 install --upgrate pip`
    + virtual env
        + `pip3.6 install virtualenv`
        + `virtualenv venv`
    + project
        + `source venv/bin/activate`
        + `pip install -r requirement.txt`
+ Database(postgresql 10.0)
    + install
        + `rpm -Uvh https://yum.postgresql.org/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm`
        + `yum install postgresql10-server postgresql10`
        + `/usr/pgsql-10/bin/postgresql-10-setup initdb`
    + Start PostgreSQL Server
        + `ystemctl start postgresql-10.service`
        + `systemctl enable postgresql-10.service`
    + Access create db, user    
        + `su - postgres -c "psql"`
        + `create role admin_user;`
        + `alter role admin_user with login;`
        + `create database swivel;`
        + `grant all privileges on database swivel to admin_user;`
        + show all database `\l`
        + use swivel database `\c swivel`
        + show all tables `\dt`
        + exit `\q`
         
    + give user permission to access postgresql
        + `sudo nano /var/lib/psql/10/data/postgresql.conf` 
        + allow or add line `listen_address = '*'`
        
        ```
        trust
        Allow the connection unconditionally. 
        This method allows anyone that can connect to the PostgreSQL database server 
        to login as any PostgreSQL user they wish, without the need for a password or 
        any other authentication. See Section 19.3.1 for details.
        
        reject
        Reject the connection unconditionally. 
        This is useful for "filtering out" certain hosts from a group, for example a 
        reject line could block a specific host from connecting, while a later line 
        allows the remaining hosts in a specific network to connect.
        
        md5
        Require the client to supply a double-MD5-hashed password for authentication. 
        See Section 19.3.2 for details.
        
        password
        Require the client to supply an unencrypted password for authentication. 
        Since the password is sent in clear text over the network, this should not 
        be used on untrusted networks. See Section 19.3.2 for details.
        
        gss
        Use GSSAPI to authenticate the user. 
        This is only available for TCP/IP connections. See Section 19.3.3 for details.
        
        sspi
        Use SSPI to authenticate the user. 
        This is only available on Windows. See Section 19.3.4 for details.
        
        ident
        Obtain the operating system user name of the client by contacting the ident 
        server on the client and check if it matches the requested database user name. 
        Ident authentication can only be used on TCP/IP connections. When specified 
        for local connections, peer authentication will be used instead. 
        See Section 19.3.5 for details.
        
        peer
        Obtain the client's operating system user name from the operating system 
        and check if it matches the requested database user name. 
        This is only available for local connections. See Section 19.3.6 for details.
        
        ldap
        Authenticate using an LDAP server. See Section 19.3.7 for details.
        
        radius
        Authenticate using a RADIUS server. See Section 19.3.8 for details.
        
        cert
        Authenticate using SSL client certificates. See Section 19.3.9 for details.
        
        pam
        Authenticate using the Pluggable Authentication Modules (PAM) service provided 
        by the operating system. See Section 19.3.10 for details.

        ```    
 + Service   
    + frontend
        + create the service named frontend (port: 4200)\
        `sudo nano /etc/systemd/system/frontend.service`

            ```
            [Unit]
            Description=Serve for swivel frontend
            After=network.target

            [Service]
            User=root
            WorkingDirectory=/root/Caleo/frontend
            ExecStart=/usr/bin/npm start

            [Install]
            WantedBy=multi-user.target
            ```
        + start, restart, deamon-reload, stop, status
            ```
            sudo systemctl start frontend
            sudo systemctl restart frontend
            sudo systemctl stop frontend
            sudo systemctl status frontend
            sudo systemctl deamon-relaod
            ``` 
    + Backend
        + create the service named backend
            + `pip install gunicorn`
            + `pip install eventlet`
            + `sudo nano /etc/systemd/system/backend.service`

                ```
                [Unit]
                Description=Gunicorn instance to serve swivel
                After=network.target
                
                [Service]
                User=root
                WorkingDirectory=/root/Caleo/backend
                Environment="PATH=/root/Caleo/backend/venv/bin"
                ExecStart=/root/Caleo/backend/venv/bin/gunicorn -w 3 --bind 0.0.0.0:8080 backend.wsgi
                [Install]
                WantedBy=multi-user.target
                ```
        + start, restart, deamon-reload, stop, status
            ```
            sudo systemctl start backend
            sudo systemctl restart backend
            sudo systemctl stop backend
            sudo systemctl status backend
            sudo systemctl deamon-reload
            ```
    + nginx
        + install
            + `sudo yum install epel-release`
            + `sudo yum install nginx`
            + `sudo nano /etc/nginx/nginx.conf`
            + disabled server block
        + config
            + `sudo nano /etc/nginx/conf.d/swivel.conf`
            ```
            server {
             listen 80;
             server_name swivel.net;
             location / {
                 include proxy_params;
                 proxy_pass http://localhost:4200;
             }
             location /api/ {
                 include proxy_params;
                 proxy_pass http://localhost:8080/api/;
             }
            }
            
            ```
          
          
### Contact Me
+ Name: Jason Halog
+ Email: certainty15750@yahoo.com
+ Profile: https://www.upwork.com/o/profiles/users/~0157582bfc2c74c01c/
