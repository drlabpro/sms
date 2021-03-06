a
    ���_�  �                   @   s�   d dl Z d dlZdd� Zdd� Zdd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zedkr�e�  dS )�    Nc                  C   s�   t �d� d} td� t�  td� t�  td�}t�|�� �}|�� }|| krpt�  td� t �d� t�  n td� td	� t �d
� t	�  d S )N�clearZ 257bd922a614ae23238271abfc096567z 	 SCHOOL MANAGEMENT SYSTEM z Continue using passwordz Enter Your Password : z Password Matched �sleep 0.5 && clearz Incorrect Password Entered z	 Exiting zsleep 1)
�os�system�print�input�hashlibZmd5�encodeZ	hexdigest�menu�exit)�pwdZepwd�result�final� r   �main.py�main   s$    


r   c                  C   s�   t d� t �  t d� t d� t d� t d� t d� t d� t d� t �  t �  td	�} | d
krjt�  nh| dkrzt�  nX| dkr�t�  nH| dkr�t�  n8| dkr�t�  n(| dkr�t�  n| dkr�t�  nt d� d S )Nz	 	 SCHOOL MANAGEMENT SYSTEM z 1. Admit Teachers z 2. Admit Students � 3. Show Teachers z 4. Show Students z 5. Setting z
 6. About z	 7. Exit �Enter your Choice : �1�2�3�4�5�6�7� Invalid Input )	r   r   �	teachmenu�studmenu�	showteach�showstud�setting�aboutr   )Zc1r   r   r   r
      s6    r
   c                  C   s�   t �d� td� t�  td� td� td� t�  td� t�  td�} | dkr\t�  n>| d	krlt�  n.| d
kr|t�  n| dkr�t�  ntd� t�  d S )Nr   z	 	 Teachers Area  z 1. Add Limited Teachers z 2. Add Unlimited Teachers r   � 4. Main Menu r   r   r   r   r   zInvalid Input)	r   r   r   r   �	addlteachZaddteachr   r
   r   )�c2r   r   r   r   :   s(    
r   c                  C   s�   t �d� td� t�  td� td� td� t�  td� ttd��} | dkrZt�  n>td	krjt�  n.td
krzt�  ntdkr�t	�  ntd� t
�  d S )Nr   z	 	 Students Area  z 1. Add Limited Students z 2. Add Unlimited Students z 3. Show Students r"   r   r   r   r   r   r   )r   r   r   �intr   �addlstudr$   �addstudr   r
   r   )Zc3r   r   r   r   S   s&    
r   c                  C   st   t �d� td� t�  td�} | �� }tdd�}|�� }t|�}|d }t|d� t�  t|� | ��  t�  d S )Nr   z Teacher Details �teachdet.txt�r�   z Teachers Record Founded �	r   r   r   �open�read�	readlines�len�closer
   )�	teachfileZ	teachcontZmyfile�s�countZtcountr   r   r   r   k   s    


r   c                  C   sn   t �d� td� td�} | �� }tdd�}|�� }t|�}|d }t|d� t�  t|� | ��  t�  d S )Nr   z Students Detail �studdet.txtr)   r*   z Students Record Founded r+   )�studfileZstudcontZs2fileZs2linesZs2tcountZs2countr   r   r   r   |   s    


r   c                   C   s$   t �d� td� td� t�  d S )Nr   z	 	 	  ABOUT 
 aW  This Software is developed by DEVESH SINGH on Date Sunday 31 November 2020 With Love in India.

This ( SCHOOL MANAGEMENT SYSTEM ) software helps you to save and track teachers details , sallery and students information in simple fast and relaible way.

FEATURES
1 Add Definef number of teacher and students
2 Add unlimited teachers and students at a time
3 Show Teacher and Students details in mannerised way.
4 Easy to customisable ( Premium )

If you have any more ideas on features or find any bug or problem feel free to contact me at username@domain.extension.
Thank you for choosing my work 

�r   r   r   r
   r   r   r   r   r!   �   s    
r!   c                   C   s*   t �d� td� t �d� t j��  d S )Nr   z[!]   Closing this system..zsleep 1 && clear)r   r   r   �sysr   r   r   r   r   r   �   s    

r   c                  C   s�   t td��} tdd�}t| �D ]h}t�  td|d d� td�}td�}td	�}td
�}d| d | d | d | d }|�|� q|��  t�  td� t�  t�  d S )NzEnter number of Teachers : r(   �a+zEnter details of Teacher �   �	 below : �Enter Name : zEnter Post : zEnter Sallery : �Enter Address : �Name : z
Post : z
Sallery : �
Address : �
 
z Details Saved )r%   r   r,   �ranger   �writer0   r   )Zn2r1   �i�nameZpostZsall�addr�detr   r   r   r#   �   s     
$r#   c                   C   s   t d� d S )Nz Program Coming Soon �r   r   r   r   r   �addtech�   s    rG   c                  C   s�   t td��} tdd�}t| �D ]h}t�  td|d d� td�}td�}td	�}td
�}d| d | d | d | d }|�|� q|��  t�  td� t�  t�  d S )NzEnter number of Students : r4   r8   z Enter details of Student r9   r:   r;   zEnter Class: zEnter Roll Number : r<   r=   z	
Class : z
Roll Number : r>   r?   z Details Saved)r%   r   r,   r@   r   rA   r0   r   )Zn3r5   rB   rC   ZclasZrollrD   rE   r   r   r   r&   �   s     
$r&   c                   C   s   t d� d S )Nz Program coming soonrF   r   r   r   r   r'   �   s    r'   c                   C   s"   t �d� td� t�  t�  d S )Nr   zWork in progressr6   r   r   r   r   r    �   s    
r    �__main__)r   r   r   r
   r   r   r   r   r!   r   r#   rG   r&   r'   r    �__name__r   r   r   r   �<module>   s     