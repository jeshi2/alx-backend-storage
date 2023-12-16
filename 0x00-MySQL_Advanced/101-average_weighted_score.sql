-- Create a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id_val INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor for users
    OPEN cur;

    -- Loop through each user and compute average weighted score
    read_loop: LOOP
        FETCH cur INTO user_id_val;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Call the individual user computation procedure
        CALL ComputeAverageWeightedScoreForUser(user_id_val);
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;