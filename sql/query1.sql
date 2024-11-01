WITH first_reports AS (
    SELECT user_id, MIN(created_at) AS first_report_date
    FROM reports
    GROUP BY user_id
),
filtered_users AS (
    SELECT user_id
    FROM first_reports
    WHERE first_report_date >= '2021-01-01' AND first_report_date < '2022-01-01'
)
SELECT user_id, SUM(reward) AS total_reward_2022
FROM reports
WHERE user_id IN (SELECT user_id FROM filtered_users)
  AND created_at >= '2022-01-01' AND created_at < '2023-01-01'
GROUP BY user_id;
