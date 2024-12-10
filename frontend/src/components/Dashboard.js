import React from 'react';

function Dashboard() {
return (
<div>
    <h2>Analytics Dashboard</h2>
    <iframe 
        src="http://grafana.local/d/your_dashboard_id/your_dashboard_name?orgId=1&refresh=10s" 
        width="100%" 
        height="800px"
        style={{ border: 0 }}
    />
</div>
);
}

export default Dashboard;