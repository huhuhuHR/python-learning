achievement = '''
    create table achievement(
        id bigint(20) NOT NULL AUTO_INCREMENT,
        idcard varchar(255)  DEFAULT NULL,
        name varchar(255)  DEFAULT NULL,
        chinese varchar(255)  DEFAULT NULL,
        math varchar(255)  DEFAULT NULL,
        english varchar(255)  DEFAULT NULL,
        multiple varchar(255)  DEFAULT NULL,
        total varchar(255)  DEFAULT NULL,
        RIMARY KEY (`id`) USING BTREE
    )ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
'''
if __name__ == '__main__':
    print(achievement)
