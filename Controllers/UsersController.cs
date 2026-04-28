using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MusicApp.Backend.Models;
using BCrypt.Net; 

namespace MusicApp.Backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private readonly MusicAppDbContext _context;

        public UsersController(MusicAppDbContext context)
        {
            _context = context;
        }

        public class RegisterRequest
        {
            public string Username { get; set; } = null!;
            public string Password { get; set; } = null!;
            public string Email { get; set; } = null!;
        }
        public class LoginRequest
        {
        public string Username { get; set; } = null!;
        public string Password { get; set; } = null!;
        }

        [HttpPost("register")]
        public async Task<IActionResult> Register([FromBody] RegisterRequest request)
        {
            // 1. Kiểm tra trùng Username
            var userExists = await _context.Users.AnyAsync(u => u.Username == request.Username);
            if (userExists)
                return BadRequest(new { message = "Tên đăng nhập đã tồn tại!" });

            // 2. Mã hóa mật khẩu (Hash)
            // Lưu ý: Dùng BCrypt.Net.BCrypt để chỉ định rõ thư viện nếu bị mờ
            string passwordHash = BCrypt.Net.BCrypt.HashPassword(request.Password);

            // 3. Lưu User (Dùng đúng tên PasswordHash như trong file User.cs của bạn)
            var newUser = new User
            {
                Username = request.Username,
                PasswordHash = passwordHash, 
                Email = request.Email
            };

            _context.Users.Add(newUser);
            await _context.SaveChangesAsync();

            return Ok(new { message = "Đăng ký thành công!" });
        }
        [HttpPost("login")]
public async Task<IActionResult> Login([FromBody] LoginRequest request)
{
    // 1. Tìm user theo tên đăng nhập
    var user = await _context.Users.FirstOrDefaultAsync(u => u.Username == request.Username);

    // 2. Kiểm tra mật khẩu (So sánh mật khẩu trần với mật khẩu đã băm trong DB)
    if (user == null || !BCrypt.Net.BCrypt.Verify(request.Password, user.PasswordHash))
    {
        return Unauthorized(new { message = "Tên đăng nhập hoặc mật khẩu không chính xác!" });
    }

    // 3. Đăng nhập thành công
    return Ok(new { 
        message = "Đăng nhập thành công!", 
        user = new { user.Id, user.Username, user.Email } 
    });
}
    }
}