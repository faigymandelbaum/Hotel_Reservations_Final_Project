SELECT TOP 10 *
FROM Reservation r
JOIN Guest g
ON r.GuestId = g.GuestId
WHERE r.agent = (SELECT TOP 1 r.agent
	FROM Reservation r
	JOIN Guest g
	ON r.GuestId = g.GuestId
	WHERE g.country = 'GBR' and r.agent != 'no agent'
	GROUP BY r.agent
	ORDER BY COUNT(r.agent) DESC) and r.GuestId = g.GuestId and g.country = 'GBR';

SELECT *
FROM Reservation r
JOIN Guest g
ON g.GuestId = r.GuestId
WHERE YEAR(reservation_status_date) = 2015 and adr BETWEEN 150 AND 200 and is_canceled != 1;

SELECT g.children, AVG(r.stays_in_weekend_nights + r.stays_in_week_nights) AS average_nights
FROM Reservation r
JOIN Guest g
ON r.GuestId = g.GuestId
GROUP BY g.children;

With CTE as
 (SELECT TOP 1 agent, count(*) as c
 from Reservation as r
 JOIN Guest as g
 On r.GuestId = g.GuestId
 WHERE g.Country='PRT'
 GROUP BY agent
 Order By c desc)
 --AGENT IS 240
 SELECT TOP 10 * from Reservation as r
 JOIN Guest as g
 ON r.GuestId = g.GuestId
 WHERE g.Country='PRT'
 AND r.agent = (SELECT agent FROM CTE);

with cases AS
(SELECT  *, CASE WHEN agent != 'no agent' THEN 'agent'
			   WHEN company != 'no company' THEN 'company'
			   WHEN direct_booking = 'yes' THEN 'direct_booking'
			   END AS booked_through
FROM Reservation)

SELECT booked_through, COUNT(booked_through) amount_booked
FROM cases
WHERE YEAR(arrival_date) = (SELECT TOP 1 YEAR(arrival_date) FROM Reservation
GROUP BY YEAR(arrival_date)
ORDER BY COUNT(YEAR(arrival_date)) DESC)
GROUP BY booked_through;





