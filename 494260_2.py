import sys
import heapq # heapq is a built-in library for priority queues

def solve_molecules():
    # Read N, M, K
    try:
        n_str, m_str, k_str = sys.stdin.readline().split()
        N, M, K = int(n_str), int(m_str), int(k_str)
    except (IOError, ValueError):
        return
        
    # Read source and target
    s_str, t_str = sys.stdin.readline().split()
    S, T = int(s_str), int(t_str)

    # Adjacency list for interactions
    adj = {i: [] for i in range(N)}
    for _ in range(M):
        u_str, v_str, z_str = sys.stdin.readline().split()
        u, v, z = int(u_str), int(v_str), int(z_str)
        adj[u].append((v, z))

    # Set for forbidden transitions
    forbidden = set()
    for _ in range(K):
        u_str, v_str, w_str = sys.stdin.readline().split()
        u, v, w = int(u_str), int(v_str), int(w_str)
        forbidden.add((u, v, w))

    # --- A* Search Implementation ---
    # Priority queue: (cost, current_node, prev_node)
    pq = [(0, S, -1)]
    # dist: (current_node, prev_node) -> cost
    dist = {(S, -1): 0}
    
    min_cost_to_T = float('inf')

    while pq:
        cost, curr_node, prev_node = heapq.heappop(pq)
        
        # Optimization: If we've already found a cheaper path to T,
        # we can skip this one.
        if cost > min_cost_to_T:
            continue
        
        # Check if we've reached the target
        if curr_node == T:
            min_cost_to_T = min(min_cost_to_T, cost)
            continue
            
        # Explore neighbors
        if curr_node in adj:
            for neighbor, weight in adj[curr_node]:
                # Check for forbidden transition
                if (prev_node, curr_node, neighbor) in forbidden and neighbor != T:
                    continue

                new_cost = cost + weight
                state = (neighbor, curr_node)
                
                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, curr_node))

    if min_cost_to_T == float('inf'):
        print(-1)
    else:
        print(min_cost_to_T)

# The following is for local testing
if __name__ == "__main__":
    solve_molecules()
