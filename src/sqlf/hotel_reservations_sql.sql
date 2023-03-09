SELECT TOP 10 r.* , g.*
FROM Reservation r
JOIN Guest g
ON r.GuestId = g.GuestId
join (SELECT TOP 1 agent, COUNT(agent) AS num_bookings
	FROM Reservation 
	WHERE country = 'PRT' and agent != 'no agent'
	GROUP BY agent
	ORDER BY num_bookings DESC) top_agent
ON top_agent.agent = R.agent
WHERE r.agent = top_agent.agent and r.guestId = g.GuestId;

SELECT *
FROM Reservation r
JOIN Guest g
ON g.GuestId = r.GuestId
WHERE YEAR(reservation_status_date) = 2015 and adr BETWEEN 150 AND 200 and is_canceled != 0;

SELECT g.children, AVG(r.stays_in_weekend_nights + r.stays_in_week_nights) AS average_nights
FROM Reservation r
JOIN Guest g
ON r.GuestId = g.GuestId
GROUP BY g.children
