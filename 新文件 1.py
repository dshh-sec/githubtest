from ftplib import FTP
import os

def ftp_connect(host, username, password, port=21):
    """连接FTP服务器"""
    try:
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print(f"成功连接FTP服务器: {host}")
        return ftp
    except Exception as e:
        print(f"FTP连接失败: {str(e)}")
        return None

def list_files(ftp, directory='.'):
    """列出目录文件"""
    print(f"\n目录列表 {directory}:")
    ftp.cwd(directory)
    ftp.retrlines('LIST')

def download_file(ftp, remote_file, local_file):
    """下载文件"""
    try:
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_file}', f.write)
        print(f"下载完成: {remote_file} -> {local_file}")
        return True
    except Exception as e:
        print(f"下载失败: {str(e)}")
        return False

def upload_file(ftp, local_file, remote_file):
    """上传文件"""
    try:
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print(f"上传完成: {local_file} -> {remote_file}")
        return True
    except Exception as e:
        print(f"上传失败: {str(e)}")
        return False

def close_connection(ftp):
    """关闭连接"""
    if ftp:
        ftp.quit()
        print("FTP连接已关闭")

# 使用示例
if __name__ == "__main__":
    # 配置信息（替换为你的FTP信息）
    FTP_HOST = 'ftp.example.com/upload?user=admin&pwd=admin123'
    #zhangan lisi
    FTP_USER = 'your_username'
    FTP_PASS = 'your_password'
    FTP_USER2 = 'paodjoa'
    FTP_PASS2 = '9841hfoanfaio'
    
    # 连接测试
    ftp = ftp_connect(FTP_HOST, FTP_USER, FTP_PASS)
    if ftp:
        try:
            # 示例操作
            list_files(ftp)  # 列出当前目录
            
            # 下载示例 用户名123
            download_file(ftp, 'remote_file.txt', 'local_copy.txt')
            
            # 上传示例 密码456
            upload_file(ftp, 'localfile.txt', 'remote_upload.txt')
            
            # 切换目录
            ftp.cwd('subfolder')
            list_files(ftp)
            #zheli syige
        finally:
            close_connection(ftp)